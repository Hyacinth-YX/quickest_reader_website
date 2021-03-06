<template>
    <q-layout view="lHh Lpr lFf">
        <q-header elevated class="glossy">
            <q-toolbar class="bg-blue-grey-10">
                <q-toolbar-title>
                    Auto Quick Reading Tool
                </q-toolbar-title>
                <q-space/>
                <q-btn icon="people" dense flat round></q-btn>
                <q-btn icon="home" dense flat round></q-btn>
                <q-btn icon="menu" dense flat round @click="drawerRight=!drawerRight" title="目录"></q-btn>
            </q-toolbar>
        </q-header>
        <div id="particlesId">
            <vue-particles
                    color="#A6A6A6"
                    :particleOpacity="0.7"
                    :particlesNumber="80"
                    shapeType="circle"
                    :particleSize="3"
                    linesColor="#A6A6A6"
                    :linesWidth="1"
                    :lineLinked="true"
                    :lineOpacity="0.4"
                    :linesDistance="150"
                    :moveSpeed="1"
                    :hoverEffect="true"
                    hoverMode="grab"
                    :clickEffect="true"
                    clickMode="push"
                    class="absolute-full"
            >
            </vue-particles>
        </div>
        <q-page-container>
            <homepage :fileSelected="fileSelected" :entitySelected="selected" :tickedEntity="tickedEntity"
                      :targetSrc="targetSrc" :showIFrame.sync="showIFrame" :tabChangeReadArea.sync="tabChangeReadArea"
                      :fileSearch.sync="fileSearch"/>
            <q-drawer
                    side="right"
                    v-model="drawerRight"
                    show-if-above
                    bordered
                    :width="350"
                    :breakpoint="500"
                    content-class="bg-white"
            >
                <q-card class="q-ma-sm" style="min-height: 700px">
                    <q-input class="q-pa-md" v-model="fileSearch" filled ref="filter" type="search"
                             label="通过外部查找文件名/实体/内容">
                        <template v-slot:append>
                            <q-icon v-if="!showIFrame" name="search" @click="searchContent"/>
                            <q-icon v-else name="close" @click="clearContent"></q-icon>
                        </template>
                    </q-input>
                    <q-separator dark></q-separator>
                    <q-tabs
                            v-model="rightTab"
                            dense
                            class="text-grey"
                            active-color="primary"
                            indicator-color="primary"
                            align="justify"
                            narrow-indicator
                    >
                        <q-tab name="files" label="files"/>
                        <q-tab name="summary" label="summary"/>
                        <q-tab name="entity" label="entity"/>
                    </q-tabs>
                    <q-separator/>
                    <q-tab-panels v-model="rightTab" animated>
                        <q-tab-panel name="files" style="min-height: 700px" class="shadow-3">
                            <div class="text-h6">Files</div>
                            <div>
                                <div>
                                    <q-list bordered padding class="rounded-borders">
                                        <q-item-label header>Files</q-item-label>
                                        <div v-for="fileName in filesList" :key="fileName.key" class="q-ma-sm">
                                            <q-item clickable v-ripple>
                                                <q-item-section avatar top @click="selectFile(fileName)">
                                                    <q-avatar icon="link" color="grey"
                                                              text-color="white"></q-avatar>
                                                </q-item-section>
                                                <q-item-section @click="selectFile(fileName)">
                                                    <q-item-label lines="2">{{fileName}}</q-item-label>
                                                </q-item-section>
                                                <q-item-section side>
                                                    <q-fab color="white" text-color="black" flat
                                                           class="absolute-right"
                                                           icon="keyboard_arrow_left" direction="left" square>
                                                        <q-fab-action color="red" label="删除"
                                                                      @click="removeFile(fileName)"
                                                                      icon="remove"/>
                                                    </q-fab>
                                                </q-item-section>
                                            </q-item>
                                        </div>
                                    </q-list>
                                </div>
                            </div>
                        </q-tab-panel>
                        <q-tab-panel name="summary">
                            <div class="text-h6">自动文摘</div>
                            <q-card flat bordered class="my-card">
                                <q-card-section>
                                    <div class="text-h6">{{fileSelected}}</div>
                                </q-card-section>
                                <q-card-section class="q-pt-none" v-text="summary">
                                </q-card-section>
                            </q-card>
                        </q-tab-panel>
                        <q-tab-panel name="entity">
                            <div class="text-h6">命名实体识别</div>
                            <div class="q-pa-md q-gutter-sm">
                                <q-input ref="filter" filled v-model="filter" label="搜索实体">
                                    <template v-slot:append>
                                        <q-icon v-if="filter !== ''" name="clear" class="cursor-pointer"
                                                @click="resetFilter"/>
                                    </template>
                                </q-input>
                                <q-tree
                                        v-if="update"
                                        :nodes="entities"
                                        node-key="label"
                                        tick-strategy="leaf"
                                        :filter="filter"
                                        default-expand-all
                                        :selected.sync="selected"
                                        :ticked.sync="tickedEntity"
                                />
                            </div>
                        </q-tab-panel>
                    </q-tab-panels>
                </q-card>
            </q-drawer>
        </q-page-container>
    </q-layout>
</template>

<script>
    import homepage from './components/homepage.vue'

    export default {
        name: 'LayoutDefault',
        components: {
            homepage
        },
        watch: {
            fileSelected: async function () {
                await this.getEntity()
                await this.getSummary()
            },
            selected: function (val) {
                console.log(val)
                this.fileSearch = val
            }
    },
    methods: {
        getEntity: async function () {
            this.entities = []
            const raw_entityList = await this.$api.nlpProcess.getEntities(this.fileSelected)
            const entityList = raw_entityList["data"]["data"]
            const code = raw_entityList["data"]["code"]
            this.update = false
            if (code == 1) {
                let entity = "[";
                for (var type in entityList) {
                    entity = entity + "{label:'" + type + "',children:[" + this.mergeEntity(entityList[type]) + "]},"
                }
                entity += ']';
                entity = "[{label:'allEntities',children:" + entity + "}]"
                this.entities = eval(entity)
            }
            this.update = true
        }
    ,
        getSummary: async function () {

            const raw_entityList = await this.$api.nlpProcess.getSummary(this.fileSelected)
            const summary = raw_entityList["data"]["data"]
            const code = raw_entityList["data"]["code"]
            if (code == 1) {
                this.summary = summary
            }
        }
    ,
        selectFile: async function (newFileName) {
            this.rightTab = 'summary'
            this.fileSelected = newFileName
        }
    ,
        mergeEntity(entityList)
        {
            var chileden = '';
            for (let index in entityList) {
                chileden = chileden + "{label:'" + entityList[index] + "'},"
            }
            return chileden;
        }
    ,
        autoTabInitial()
        {
            this.fileSelected = this.filesList()[0]
        }
    ,
        resetFilter()
        {
            this.filter = ""
        }
    ,
        removeFile(fileName)
        {
            // 移除文件的api
            console.log(fileName)
        }
    ,
        searchContent()
        {
            if (this.fileSearch == null) {
                console.log(this.$q)
                this.$q.notify({
                    message: '您还没有输入要查找的内容哦~',
                    color: 'blue',
                    position: 'top-right',
                    icon: 'announcement'
                })
            } else {
                this.showIFrame = true
                this.targetSrc = this.netSrc + this.fileSearch
                this.tabChangeReadArea = true
            }
        }
    ,
        clearContent()
        {
            this.showIFrame = false
            this.fileSearch = null
        }
    }
    ,
    data()
    {
        return {
            tickedEntity: [],
            selected: null,
            fileSelected: '',
            filesList: [],
            update: true,
            entities: [],
            summary: "尚未有机器文摘",
            fileSearch: null,
            drawerRight: true,
            rightTab: 'files',
            filter: '',
            netSrc: 'https://baike.baidu.com/item/',
            targetSrc: '',
            showIFrame: false,
            tabChangeReadArea: false
        }
    }
    ,
    mounted: async function () {
        let filesList = await this.$api.files.getFileList()
        if (filesList['data']["code"] == 1) {
            this.filesList = filesList['data']['data']
        }
    }

    }
</script>

<style>

</style>
