<template>
    <div>
        <q-splitter
                v-model="tabSplitterModel"
        >
            <template v-slot:before>
                <q-tabs
                        v-model="tab"
                        vertical
                        class="text-blue-4 row justify-start"
                        align="justify"
                        dense
                        :breakpoint="0"
                        style="min-height: 700px"
                >
                    <q-tab class="col-12" name="loadFiles" icon="mail" label="上传文件"/>
                    <q-tab class="col-12" name="mindGraph" icon="map" label="思维导图总览"/>
                    <q-tab class="col-12" name="readArea" icon="movie" label="快速浏览"/>
                </q-tabs>
            </template>

            <template v-slot:after>
                <q-tab-panels
                        v-model="tab"
                        animated
                        transition-prev="jump-up"
                        transition-next="jump-up"
                        align="center"
                >
                    <q-tab-panel name="loadFiles">
                        <div class="text-h1 q-ma-lg" style="font-family: 'Adobe Caslon Pro'; ">
                            <div class="flex-center"><span class="text-cyan">SPeeD</span><span
                                    class="text-accent">ReaD!</span></div>
                        </div>
                        <div class="q-ma-lg q-mt-xl  shadow-3" style="width: 300px">
                            <q-uploader
                                    ref="uploader"
                                    label="上传需要转化的文件"
                                    :url="upload_url"
                                    multiple
                                    method="POST"
                                    :factory="uploadFile"
                                    hide-upload-button
                                    @failed="uploadFailed"
                                    @uploaded="uploaded"
                                    batch="batch"
                                    style="max-width: 300px"
                                    color="amber"
                                    text-color="black"
                                    accept=".txt"
                                    auto-upload
                            />
                        </div>
                        <q-card>
                            <div>
                                <q-tabs
                                        v-model="startTab"
                                        dense
                                        class="bg-grey-3 text-grey-7"
                                        active-color="primary"
                                        indicator-color="purple"
                                        align="justify"
                                >
                                    <q-tab name="start" label="Hello world"/>
                                    <q-tab name="mid" label="start up"/>
                                    <q-tab name="back" label="about us"/>
                                </q-tabs>

                                <q-tab-panels v-model="startTab" animated class="bg-blue-5 text-white">
                                    <q-tab-panel name="start">
                                        <div class="text-h6">Mails</div>
                                        <div class="text-body1" align="left">Hi! There!</div>
                                        <div class="text-body2" align="left">
                                            欢迎使用基于自然语言处理的快速文本阅读器，在这里你可以借助新奇的自然语言处理技术快速阅读你的文章。通过命名实体识别，你可以按照实体类别快速找到文中提到的实体；借助由关系抽取生成的思维导图，你能够迅速把握文章脉络；当你只是想看一看文章主题内容的时候，你可以选择自动文摘功能，主题内容自动归纳，精准而快速。
                                        </div>

                                    </q-tab-panel>

                                    <q-tab-panel name="mid">
                                        <div class="text-h6">Tips</div>
                                        <div class="text-body2" align="left">
                                            要使用该阅读器，您需要先将自己想要阅读的文件上传到我们的网站上（上传入口就在上面）。系统会自动分析您上传的文件，并返回给您相应的提示。你可以在"思维导图"选项卡中查看生成的思维导图，并在快速阅读器中，动态地查看相关实体、定义、关系。
                                        </div>
                                        <div class="text-body2" align="left">
                                            此外我们还提供快速查询服务，当您对文中一些内容产生疑惑时，可以点击放大镜图标，通过内置的搜索框为您在互联网上找到相关信息。优先返回百度百科、维基百科等官方内容。
                                        </div>
                                    </q-tab-panel>

                                    <q-tab-panel name="back">
                                        <div class="text-h6">License</div>
                                        本作品所有内容都获得相应许可，结合开源代码构建而成。希望您学习愉快~
                                        <q-separator spaced dark color="blue-5"></q-separator>
                                        <q-btn class="q-ma-md text-h4 bg-white text-accent shadow-3" rounded
                                               label="Start Using!" @click="startUsing"></q-btn>
                                    </q-tab-panel>
                                </q-tab-panels>
                            </div>
                        </q-card>
                    </q-tab-panel>

                    <q-tab-panel name="mindGraph">
                        <mind-graph :fileSelected="fileSelected"></mind-graph>
                    </q-tab-panel>

                    <q-tab-panel name="readArea">
                        <div>
                            <read-area :fileSelected="fileSelected" :entitySelected="entitySelected"
                                       :tickedEntity="tickedEntity" :targetSrc="targetSrc"
                                       :showIFrame.sync="showIFrame" :fileSearch.sync="fileSearch"></read-area>
                        </div>

                    </q-tab-panel>
                </q-tab-panels>
            </template>

        </q-splitter>
    </div>
</template>


<script>
    import readArea from "../components/readArea";
    import mindGraph from "../components/mindGraph";
    import {host} from "../utils/http";

    export default {
        name: 'homepage',
        props: {
            fileSelected: String,
            entitySelected: String,
            tickedEntity: Array,
            showIFrame: Boolean,
            targetSrc: String,
            tabChangeReadArea: Boolean,
            fileSearch: String
        },
        components: {
            readArea,
            mindGraph
        },
        data() {
            return {
                tab: 'loadFiles',
                startTab: 'start',
                tabSplitterModel: 1,
                listSplitterModel: 1,
                upload_url: ""
            }
        },
        watch: {
            tabChangeReadArea: function (val) {
                if (val) {
                    this.tab = "readArea"
                    this.tabChangeReadArea = false
                }
            }
        },
        methods: {
            uploaded: async function () {
                location.reload()
                console.log("start analyze..." + this.fileSelected)
                await this.$api.nlpProcess.analyze(this.fileSelected)
            },
            startUsing() {
                this.$refs.uploader.pickFiles()
            },
            uploadFailed(req) {
                console.log('failed', req)
            },
            uploadFile: async function (file) {
                this.$q.notify({
                    message: '正在上传~请等待自动刷新',
                    color: 'blue',
                    position: 'top-right',
                    icon: 'announcement'
                })
                file = file[0]
                let filename = file.name
                let data = await this.getTxtText(file)
                const url = host.first + "/files/upload"
                this.upload_url = url
                this.fileSelected = filename
                return new Promise((resolve) => {
                    console.log('text', data)
                    resolve({
                        url: host.first + "/files/upload",
                        method: 'POST',
                        // headers: [{name: 'Content-Type', value: 'application/x-www-form-urlencoded;charset=utf-8'}],
                        fields: [{name: 'data', value: data}]
                    })
                })
            },
            getTxtText(file) {
                return new Promise((resolve, reject) => {
                    const reader = new FileReader()
                    // reader.onloadend = (e) => resolve(imageToDataUri(e, 400, 400)); todo
                    reader.readAsText(file, 'utf-8')
                    reader.onload = () => resolve(reader.result)
                    reader.onerror = error => reject(error)
                })
            }
        }
    }
</script>


<style>
</style>
