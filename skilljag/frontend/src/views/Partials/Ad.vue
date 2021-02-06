<template>
  <v-sheet
    rounded="lg"
    min-height="268"
    style="
      min-height: 468px;
      position: static;
      top: 75px;
      overflow-y: auto;
      max-height: 84vh;
      opacity: 1;
    "
  >
    <h5 class="pa-10" v-if="false">Ad</h5>
    <v-img v-if="true" max-height=" 84vh" :src="ads[Math.floor(Math.random() * ads.length)]"></v-img>
  </v-sheet>
</template>

<script>
export default {
    data:()=>({
      ads:[
        '/media/images/poster/1.jpg',
        'media/images/poster/2.jpg',
        // '/images/poster/ad2test4.png',
        ]
    }),
};
</script>

