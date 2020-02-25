<template>
    <q-layout view="lHh Lpr lFf">
        <q-header elevated class="glossy">
            <q-toolbar class="bg-blue-grey-10">
                <q-toolbar-title>
                    Auto Quick Reading Tool
                </q-toolbar-title>
                <q-space/>
                <q-btn icon="people" dense flat round></q-btn>
                <q-btn icon="home" dense flat round></q-btn>
                <q-btn icon="menu" dense flat round @click="drawerRight=!drawerRight" title="待阅读材料"></q-btn>
            </q-toolbar>
        </q-header>
        <div id="particlesId">
            <vue-particles
                    color="#A6A6A6"
                    :particleOpacity="0.7"
                    :particlesNumber="80"
                    shapeType="circle"
                    :particleSize="3"
                    linesColor="#A6A6A6"
                    :linesWidth="1"
                    :lineLinked="true"
                    :lineOpacity="0.4"
                    :linesDistance="150"
                    :moveSpeed="1"
                    :hoverEffect="true"
                    hoverMode="grab"
                    :clickEffect="true"
                    clickMode="push"
                    class="absolute-full"
            >
            </vue-particles>
        </div>
        <q-page-container>
            <homepage/>
            <q-drawer
                    side="right"
                    v-model="drawerRight"
                    show-if-above
                    bordered
                    :width="300"
                    :breakpoint="500"
                    content-class="bg-white"
            >
                <q-scroll-area class="fit">
                    <div class="q-pa-sm q-ma-lg">
                        <q-input v-model="search" filled type="search" hint="查找文件名/实体/内容">
                            <template v-slot:append>
                                <q-icon name="search"/>
                            </template>
                        </q-input>
                        <q-separator dark></q-separator>
                        <q-list bordered padding class="rounded-borders" style="max-width: 350px">
                            <q-item-label header>Files</q-item-label>
                            <div v-for="n in 50" :key="n" class="q-ma-sm">
                                    <q-item clickable v-ripple>
                                        <q-item-section avatar top>
                                            <q-avatar icon="link" color="grey" text-color="white"></q-avatar>
                                        </q-item-section>
                                        <q-item-section>
                                            <q-item-label lines="2">file{{ n }} 这是文件名</q-item-label>
                                        </q-item-section>
                                        <q-item-section side>
                                            <q-fab color="white" text-color="black"  flat class="absolute-right" icon="keyboard_arrow_left" direction="left" square>
                                                <q-fab-action color="red" label="删除" @click="onClick" icon="remove"/>
                                            </q-fab>
                                        </q-item-section>
                                    </q-item>
                            </div>
                        </q-list>
                    </div>
                </q-scroll-area>
            </q-drawer>
        </q-page-container>
    </q-layout>
</template>

<script>
    import homepage from './components/homepage.vue'

    export default {
        name: 'LayoutDefault',
        components: {
            homepage
        },
        data() {
            return {
                drawerRight: true
            }
        }

    }
</script>

<style>

</style>
