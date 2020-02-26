<template>
    <div class="justify-center">
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
        components:{
            mindmap
        },
        data() {
            return {
                data: [mindGraph],
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