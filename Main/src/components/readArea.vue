<template>
    <div>
        <div class="text-h3 q-ma-md" style="font-family: AppleMyungjo; ">
            <div align="left"><span class="text-cyan">Reading</span><span
                    class="text-accent">Area</span></div>
        </div>
        <q-separator dark></q-separator>
        <!--        <q-editor v-model="editor" min-height="5rem" align="left" :toolbar="[-->
        <!--        [-->
        <!--          {-->
        <!--            label: $q.lang.editor.align,-->
        <!--            icon: $q.iconSet.editor.align,-->
        <!--            fixedLabel: true,-->
        <!--            options: ['left', 'center', 'right', 'justify']-->
        <!--          }-->
        <!--        ],-->
        <!--        ['bold', 'italic', 'strike', 'underline', 'subscript', 'superscript'],-->
        <!--        ['token', 'hr', 'link', 'custom_btn'],-->
        <!--        ['print', 'fullscreen'],-->
        <!--        [-->
        <!--          {-->
        <!--            label: $q.lang.editor.formatting,-->
        <!--            icon: $q.iconSet.editor.formatting,-->
        <!--            list: 'no-icons',-->
        <!--            options: [-->
        <!--              'p',-->
        <!--              'h1',-->
        <!--              'h2',-->
        <!--              'h3',-->
        <!--              'h4',-->
        <!--              'h5',-->
        <!--              'h6',-->
        <!--              'code'-->
        <!--            ]-->
        <!--          },-->
        <!--          {-->
        <!--            label: $q.lang.editor.fontSize,-->
        <!--            icon: $q.iconSet.editor.fontSize,-->
        <!--            fixedLabel: true,-->
        <!--            fixedIcon: true,-->
        <!--            list: 'no-icons',-->
        <!--            options: [-->
        <!--              'size-1',-->
        <!--              'size-2',-->
        <!--              'size-3',-->
        <!--              'size-4',-->
        <!--              'size-5',-->
        <!--              'size-6',-->
        <!--              'size-7'-->
        <!--            ]-->
        <!--          },-->
        <!--          {-->
        <!--            label: $q.lang.editor.defaultFont,-->
        <!--            icon: $q.iconSet.editor.font,-->
        <!--            fixedIcon: true,-->
        <!--            list: 'no-icons',-->
        <!--            options: [-->
        <!--              'default_font',-->
        <!--              'arial',-->
        <!--              'arial_black',-->
        <!--              'comic_sans',-->
        <!--              'courier_new',-->
        <!--              'impact',-->
        <!--              'lucida_grande',-->
        <!--              'times_new_roman',-->
        <!--              'verdana'-->
        <!--            ]-->
        <!--          },-->
        <!--          'removeFormat'-->
        <!--        ],-->
        <!--        ['quote', 'unordered', 'ordered', 'outdent', 'indent'],-->
        <!--        ['undo', 'redo']-->
        <!--      ]" :fonts="{-->
        <!--        arial: 'Arial',-->
        <!--        arial_black: 'Arial Black',-->
        <!--        comic_sans: 'Comic Sans MS',-->
        <!--        courier_new: 'Courier New',-->
        <!--        impact: 'Impact',-->
        <!--        lucida_grande: 'Lucida Grande',-->
        <!--        times_new_roman: 'Times New Roman',-->
        <!--        verdana: 'Verdana'-->
        <!--      }"/>-->
        <p class="reading-titile">{{fileSelected}}</p>
        <div class="reading-area">
            <div v-for="p in paragraphs" :key="p.id" v-html="p">
            </div>
        </div>
    </div>
</template>

<script>
    import $ from 'jquery';

    export default {
        name: "readArea",
        props: {
            fileSelected: String,
            entitySelected: String
        },
        data() {
            return {
                editor: '请选择一个文件',
                paragraphs: [],
                paraStyleSet: {indent: "2em", fontSize: "15px"},
            }
        },
        computed: {
            paraStyle: function () {
                let style = "text-indent:" + this.paraStyleSet.indent + ";" +
                    "font-size:" + this.paraStyleSet.fontSize + ";"
                return style

            }
        },
        watch: {
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
            entitySelected: function (val) {
                this.addBGColorTag(val)
            }
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
            addBGColorTag(targetName){
                let rep = "/" + targetName + "/g"
                let replaceHTML = "<a style='background: #eeff41'>" + targetName + "</a>"
                rep = eval(rep)
                console.log(rep)
                let that = this
                $('.reading-p').each(function(){
                    $(this).html(that.tagClean($(this).html()).replace(rep,replaceHTML))
                })
            }
        }
    }
</script>

<style lang="css" scoped>
    .reading-titile {
        text-align: center;
        font-size: 24px;
        font-family: "Songti SC";
        font-weight: bold;
    }

    .reading-area {
        text-align: left;
    }
</style>
