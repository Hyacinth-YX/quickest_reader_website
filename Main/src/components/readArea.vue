<template>
    <div>
        <div class="text-h3 q-ma-md" style="font-family: AppleMyungjo; ">
            <div align="left"><span class="text-cyan">Reading</span><span
                    class="text-accent">Area</span></div>
        </div>
        <q-separator dark></q-separator>
        <q-editor v-model="editor" min-height="5rem" align="left" :toolbar="[
        [
          {
            label: $q.lang.editor.align,
            icon: $q.iconSet.editor.align,
            fixedLabel: true,
            options: ['left', 'center', 'right', 'justify']
          }
        ],
        ['bold', 'italic', 'strike', 'underline', 'subscript', 'superscript'],
        ['token', 'hr', 'link', 'custom_btn'],
        ['print', 'fullscreen'],
        [
          {
            label: $q.lang.editor.formatting,
            icon: $q.iconSet.editor.formatting,
            list: 'no-icons',
            options: [
              'p',
              'h1',
              'h2',
              'h3',
              'h4',
              'h5',
              'h6',
              'code'
            ]
          },
          {
            label: $q.lang.editor.fontSize,
            icon: $q.iconSet.editor.fontSize,
            fixedLabel: true,
            fixedIcon: true,
            list: 'no-icons',
            options: [
              'size-1',
              'size-2',
              'size-3',
              'size-4',
              'size-5',
              'size-6',
              'size-7'
            ]
          },
          {
            label: $q.lang.editor.defaultFont,
            icon: $q.iconSet.editor.font,
            fixedIcon: true,
            list: 'no-icons',
            options: [
              'default_font',
              'arial',
              'arial_black',
              'comic_sans',
              'courier_new',
              'impact',
              'lucida_grande',
              'times_new_roman',
              'verdana'
            ]
          },
          'removeFormat'
        ],
        ['quote', 'unordered', 'ordered', 'outdent', 'indent'],
        ['undo', 'redo']
      ]" :fonts="{
        arial: 'Arial',
        arial_black: 'Arial Black',
        comic_sans: 'Comic Sans MS',
        courier_new: 'Courier New',
        impact: 'Impact',
        lucida_grande: 'Lucida Grande',
        times_new_roman: 'Times New Roman',
        verdana: 'Verdana'
      }"/>
    </div>
</template>

<script>

    export default {
        name: "readArea",
        props:{
            fileSelected:String
        },
        watch:{
            fileSelected: async function(newvalue){
              let content = await this.$api.files.getFileContent(newvalue)
              if(content["data"]["code"] == 1){
                  this.editor = content["data"]["data"]
              }
            }
        },
        data() {
            return {
                editor: '请选择一个文件'
            }
        },
        mounted: async function () {
            let content = await this.$api.files.getFileContent(this.fileSelected)
            if(content["data"]["code"] == 1){
                this.editor = content["data"]["data"]
            }
        }
    }
</script>

<style lang="css" scoped>

</style>