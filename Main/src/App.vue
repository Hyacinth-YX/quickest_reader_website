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
            <homepage/>
            <q-drawer
                    side="right"
                    v-model="drawerRight"
                    show-if-above
                    bordered
                    :width="300"
                    :breakpoint="500"
                    content-class="bg-white"
            >
                <q-card class="q-ma-sm" style="min-height: 700px">
                    <q-input class="q-pa-md" v-model="fileSearch" filled ref="filter" type="search" label="查找文件名/实体/内容">
                        <template v-slot:append>
                            <q-icon name="search"/>
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
                                <div class="">
                                    <q-list bordered padding class="rounded-borders">
                                        <q-item-label header>Files</q-item-label>
                                        <div v-for="n in 50" :key="n" class="q-ma-sm">
                                            <q-item clickable v-ripple>
                                                <q-item-section avatar top>
                                                    <q-avatar icon="link" color="grey"
                                                              text-color="white"></q-avatar>
                                                </q-item-section>
                                                <q-item-section>
                                                    <q-item-label lines="2">file{{ n }} 这是文件名</q-item-label>
                                                </q-item-section>
                                                <q-item-section side>
                                                    <q-fab color="white" text-color="black" flat
                                                           class="absolute-right"
                                                           icon="keyboard_arrow_left" direction="left" square>
                                                        <q-fab-action color="red" label="删除" @click="onClick"
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
                            Lorem ipsum dolor sit amet consectetur adipisicing elit.
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
                                        :nodes="entities"
                                        node-key="label"
                                        :filter="filter"
                                        default-expand-all
                                        :selected.sync="selected"
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
        computed: {
            entities: function () {
                //let entityList = this.$api.nlpProcess.getEntities(this.fileSelected);
                var entityList = {"address": ['a', 'b', 'c'], "book": ['d', 'e', 'f', 'g']};
                let entity = "[";
                for (var type in entityList) {
                    entity = entity + "{label:'" + type + "',children:[" + this.mergeEntity(entityList[type]) + "]},"
                }
                entity += ']';
                return eval(entity);
            }
        },
        methods: {
            mergeEntity(entityList) {
                var chileden = '';
                for (let index in entityList) {
                    chileden = chileden + "{label:'" + entityList[index] + "'},"
                }
                return chileden;
            }
        },
        data() {
            return {
                selected:null,
                fileSelected: 'test.txt',
                fileSearch:null,
                drawerRight: true,
                rightTab: 'files',
                filter: '',
                // entities:
                //     [{
                //         label: 'address',
                //         children: [
                //             {label: 'a'},
                //             {label: 'b'},
                //             {label: 'c'},]
                //     }, {
                //         label: 'book',
                //         children: [{label: 'd'}, {label: 'e'}, {label: 'f'}, {label: 'g'},]
                //     },
                //     ]
            }
        }

    }
</script>

<style>

</style>
