<template>
    <div>
        <div v-if="!showIFrame" class="text-h3 q-ma-md" style="font-family: AppleMyungjo; ">
            <div align="left"><span class="text-cyan">Reading</span><span
                    class="text-accent">Area</span></div>
        </div>
        <div v-else>
            <iframe v-if="showIFrame" :src="targetSrc" height="300px" width="900px"></iframe>
        </div>
        <q-separator dark></q-separator>
        <q-scroll-area
                :thumb-style="thumbStyle"
                :bar-style="barStyle"
                style="height: 610px; max-width: 900px;"
        >
            <p class="reading-titile shadow-5 q-pa-md">{{fileSelected}}</p>
            <div class="reading-area shadow-5 q-pa-md">
                <div v-for="p in paragraphs" :key="p.id" v-html="p">
                </div>
            </div>
        </q-scroll-area>
    </div>
</template>

<script>
    import $ from 'jquery';

    export default {
        name: "readArea",
        props: {
            fileSelected: String,
            entitySelected: String,
            tickedEntity: Array,
            showIFrame: Boolean,
            targetSrc: String,
            fileSearch: String
        },
        data() {
            return {
                editor: '请选择一个文件',
                paragraphs: [],
                paraStyleSet: {indent: "2em", fontSize: "20px"},
                searchSource: "https://www.baidu.com/baidu?wd=",
            }
        },
        computed: {
            paraStyle: function () {
                let style = "text-indent:" + this.paraStyleSet.indent + ";" +
                    "font-size:" + this.paraStyleSet.fontSize + ";"
                return style
            },
            thumbStyle () {
                return {
                    right: '4px',
                    borderRadius: '5px',
                    backgroundColor: '#027be3',
                    width: '5px',
                    opacity: 0.75
                }
            },
            barStyle () {
                return {
                    right: '2px',
                    borderRadius: '9px',
                    backgroundColor: '#027be3',
                    width: '9px',
                    opacity: 0.2
                }
            }
        },
        watch: {
            showIFrame: function (val) {
                if (val) {
                    let frame = $('iframe')
                    console.log(frame)
                }
            },
            tickedEntity: function (val) {
                // refresh the page content tag
                let that = this
                $('.reading-p').each(function () {
                    $(this).html(that.tagClean($(this).html()))
                })
                for (let index in val) {
                    this.addAccentTag(val[index])
                }
            },
            fileSelected: async function (newvalue) {
                let content = await this.$api.files.getFileContent(newvalue)
                if (content["data"]["code"] == 1) {
                    //清除文章数据中的tag标签，避免注入攻击
                    let formedContent = this.tagClean(content["data"]["data"])
                    this.editor = formedContent
                }
            },
            editor: function (val) {
                let paragraphs = val.split('\n')
                //清除原本加入的tag标签以等待加入新的标签
                this.paragraphs = this.paragraphsPreProcess(paragraphs)
            },
        },
        mounted: async function () {
            let content = await this.$api.files.getFileContent(this.fileSelected);
            if (content["data"]["code"] == 1) {
                this.editor = content["data"]["data"];
            }
        },
        methods: {
            paragraphsPreProcess(paragraphs) {
                for (let index in paragraphs) {
                    paragraphs[index] = "<p class='reading-p' style='" + this.paraStyle + "'>" +
                        paragraphs[index] + "</p>"
                }
                return paragraphs
            },
            tagClean(content) {
                let rep = /<\/?[a-zA-Z][^>]*>/g
                return content.replace(rep, "")
            },
            addAccentTag(targetName) {
                let rep = "/" + targetName + "/g"
                let replaceHTML = `<a href='#' class='entity-tag text-blue-7 bg-amber' style='font-weight: bold'>${targetName}</a>`
                rep = eval(rep)
                console.log(rep)
                $('.reading-p').each(function () {
                    $(this).html($(this).html().replace(rep, replaceHTML))
                })
            },
        }
    }
</script>

<style lang="css" scoped>
    .reading-titile {
        text-align: center;
        font-size: 30px;
        font-family: "Songti SC";
        font-weight: bold;
        background-color: rgba(246, 240, 228, 0.77);
    }

    .reading-area {
        text-align: left;
        background-color: rgba(246, 240, 228, 0.77);
    }
</style>
