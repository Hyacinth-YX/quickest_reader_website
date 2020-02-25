<template>
    <div>
        <!--        <img src="../static/siweidaotu.jpeg">-->
        <TreeChart :json="treeData"></TreeChart>
    </div>
</template>

<script>
    import TreeChart from "vue-tree-chart"
    export default {
        name: "mindGraph",
        components:{
            TreeChart
        },
        data() {
            return {
                treeData: {
                    name: 'root',
                    image_url:"https://www.baidu.com/img/baidu_resultlogo@2.png",
                    children: [
                        {
                            name: 'children1'
                        },
                        {
                            name: 'children2',
                            mate: {
                                name: 'mate',
                            },
                            children: [
                                {
                                    name: 'grandchild'
                                },
                                {
                                    name: 'grandchild2'
                                },
                                {
                                    name: 'grandchild3'
                                }
                            ]
                        },
                        {
                            name: 'children3'
                        }
                    ]
                }
            }
        }

    }
</script>

<style scoped>

</style>