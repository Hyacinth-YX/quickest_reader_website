<template>
    <div class="q-ma-md q-pa-sm bg-grey-1 col-8" id="read-area" style="height: 600px;">
        <div style="font-family: 'Heiti SC'">
        <div class="text-h1">这是一篇文章</div>
            <div v-for="n in 30" :key="n">这里是文章内容这里是文章内容这里是文
                章内容这里是文章内容这里是文章内容这里是文章内容这里是文章内容这里是文章内容这里是文章内容
                这里是文章内容这里是文章内容这里是文章内容这里是文章内容</div>
            <br>
            <div v-for="n in 30" :key="n">这里是文章内容</div>
        </div>
    </div>
</template>

<script>

    export default {
        name: "readArea"
    }
</script>

<style lang="css" scoped>

</style>