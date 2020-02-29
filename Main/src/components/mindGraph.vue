<template>
    <div class="justify-center">
        <div class="text-h3 q-ma-md" style="font-family: AppleMyungjo; ">
            <div align="left"><span class="text-cyan">MinD</span><span
                    class="text-accent">Graph</span></div>
        </div>
        <q-separator dark></q-separator>
        <mindmap
                v-model="treedata"
                :height="700"
                :width="700"
                :draggable="draggable"
                :xSpacing="xSpacing"
                :ySpacing="ySpacing"
                :gps="gps"
                v-if="update"
        ></mindmap>
    </div>
</template>

<script>
    import mindmap from "@hellowuxin/mindmap"

    export default {
        name: "mindGraph",
        props:{
            fileSelected:String
        },
        watch : {
            fileSelected : async function(){
        
                await this.loadMindGraph()
            },
        },
        methods: {
            loadMindGraph: async function(){
                 this.update = false
                 const raw = await this.$api.nlpProcess.getMindGraph(this.fileSelected)
                 const code = raw["data"]["code"]
                 const data = raw["data"]['data']
                 if (code == 1){
                     this.$set(this.treedata,0,data)
                 }
                 else{
                    this.$set(this.treedata,0,{"name":"Artical","children":[]})
                 }
                this.update = true
            }
        },
        components:{
            mindmap
        },
        computed:{
                
        },
        data() {
            return {
                draggable: true,
                xSpacing: 80,
                ySpacing: 20,
                gps: true,
                update : true,
                treedata:{"name":"Artical","children":[]}
            }
        },
        mounted : async function(){
            await this.loadMindGraph()
        }

    }
</script>

<style scoped>

</style>