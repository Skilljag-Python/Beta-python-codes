<template>
<div>
    <v-carousel
    show-arrows-on-hover
    hide-delimiter-background
    height = "auto"
    v-if="images.length>1"
    
>
        <v-carousel-item
        v-for="image in images"
        :key="image.id"
        eager
        >
            <v-img :src="image.image" contain max-height = "300px" eager></v-img>
        </v-carousel-item>
    </v-carousel>
    <v-carousel

    :show-arrows = false
    :hide-delimiter-background = "true"
     height = "auto"
    v-else-if="images.length>0">
        <v-carousel-item
        v-for="image in images"
        :key="image.id"
       >
        <v-img :src="image.image" contain max-height = "300px"></v-img>
        </v-carousel-item>
    </v-carousel>
    </div>
</template>

<script>
export default {
  name: 'PostCarousel',
  props: {
    images: Array
  }
}
</script>
