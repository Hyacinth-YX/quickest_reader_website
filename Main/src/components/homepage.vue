<template>
    <div>
        <q-splitter
                v-model="tabSplitterModel"
        >
            <template v-slot:before>
                <q-tabs
                        v-model="tab"
                        vertical
                        class="text-red-4 row justify-start"
                        align="justify"
                        dense
                        :breakpoint="0"
                        style="min-height: 700px"
                >
                    <q-tab class="col-12" name="mails" icon="mail" label="上传文件"/>
                    <q-tab class="col-12" name="alarms" icon="map" label="思维导图总览"/>
                    <q-tab class="col-12" name="movies" icon="movie" label="快速浏览"/>
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
                    <q-tab-panel name="mails">
                        <div class="text-h1 text-black  q-ma-lg" style="font-family: HYTianYuFengXingTiW; ">
                            <div class="flex-center">上传文件</div>
                        </div>
                        <div class="q-ma-lg q-mt-xl  shadow-3" style="width: 300px">
                            <q-uploader
                                    url="http://localhost:4444/upload"
                                    label="上传需要转化的文件"
                                    multiple
                                    batch="batch"
                                    style="max-width: 300px"
                                    color="red-5"
                                    text-color="black"

                            />
                        </div>
                    </q-tab-panel>

                    <q-tab-panel name="alarms">
                        <div class="text-h4 q-mb-md" style="font-family: HYTianYuFengXingTiW; ">思维导图整体预览</div>
                        <mind-graph></mind-graph>
                    </q-tab-panel>

                    <q-tab-panel name="movies">
                        <div class="text-h4 q-mb-md" style="font-family: HYTianYuFengXingTiW; ">快速浏览器</div>
                        <read-area></read-area>
                    </q-tab-panel>
                </q-tab-panels>
            </template>

        </q-splitter>
        <q-separator vertical>

        </q-separator>
        som
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
                tab: 'mails',
                tabSplitterModel: 1,
                listSplitterModel: 1
            }
        }
    }
</script>


<style>
</style>