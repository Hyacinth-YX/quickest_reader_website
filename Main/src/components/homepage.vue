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
                                    url="http://localhost:8080/files/"
                                    label="上传需要转化的文件"
                                    multiple
                                    :factory="uploadFile"
                                    @failed="uploadFailed"
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
                                        v-model="tab2"
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

                                <q-tab-panels v-model="tab2" animated class="bg-blue-5 text-white">
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
                                               label="Start Using!"></q-btn>
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
                            <read-area :fileSelected="fileSelected"></read-area>
                        </div>

                    </q-tab-panel>
                </q-tab-panels>
            </template>

        </q-splitter>
    </div>
</template>


<script>
    import '../assets/font/HYRuiYiSongW/HYRuiYiSongW.css';
    import '../assets/font/HYMiaoHunZiYouTiW/HYMiaoHunZiYouTiW.css';
    import '../assets/font/HYTianYuFengXingTiW/HYTianYuFengXingTiW.css';
    import readArea from "@/components/readArea";
    import mindGraph from "@/components/mindGraph";

    export default {
        name: 'homepage',
        props: {},
        components: {
            readArea,
            mindGraph
        },
        data() {
            return {
                tab: 'loadFiles',
                tab2: 'start',
                tabSplitterModel: 1,
                listSplitterModel: 1,
                fileSelected:'test.txt'
            }
        },
        methods: {
            uploadFailed(req){
                console.log('failed',req)
            },
            uploadFile (files) {
                // return a promise
                // eslint-disable-next-line no-debugger
                debugger
                for(let index in files){
                    let file = files[index];
                    let filename = file.name
                    return new Promise((resolve, reject) => {
                        this.getTxtText(file).then(data => {
                            // data is base64
                            console.log('file text', data)
                            // simulating a delay of 2 seconds
                            setTimeout(() => {
                                resolve(this.$api.files.fileUpload(filename,data))
                            }, 2000)
                        }).catch(() => {
                            this.$q.notify({
                                color: 'negative',
                                message: 'Failed to convert file...'
                            })
                            reject()
                        })
                    })
                }

            },
            getTxtText (file) {
                return new Promise((resolve, reject) => {
                    const reader = new FileReader()
                    // reader.onloadend = (e) => resolve(imageToDataUri(e, 400, 400))
                    reader.readAsText(file,'utf-8')
                    reader.onload = () => resolve(reader.result)
                    reader.onerror = error => reject(error)
                })
            }
        }
    }
</script>


<style>
</style>