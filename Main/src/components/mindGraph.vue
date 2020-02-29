<template>
    <div class="justify-center">
        <div class="text-h3 q-ma-md" style="font-family: AppleMyungjo; ">
            <div align="left"><span class="text-cyan">MinD</span><span
                    class="text-accent">Graph</span></div>
        </div>
        <q-separator dark></q-separator>
        <mindmap
                v-model="data"
                :height="700"
                :width="700"
                :draggable="draggable"
                :xSpacing="xSpacing"
                :ySpacing="ySpacing"
                :gps="gps"
        ></mindmap>
    </div>
</template>

<script>
    import mindGraph from '../../public/mindGraphJson/mindGraph.json'
    import mindmap from "@hellowuxin/mindmap"
    export default {
        name: "mindGraph",
        props:{
            fileSelected:String
        },
        components:{
            mindmap
        },
        computed:{
            data:function () {
                //var mindGraph = this.$api.nlpProcess.getMindGraph()
                return [mindGraph]
            }
        },
        data() {
            return {
                draggable: true,
                xSpacing: 80,
                ySpacing: 20,
                gps: true,
            }
        }

    }
</script>

<style scoped>

</style>