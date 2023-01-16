<template>
  <v-app id="inspire">
    <v-navigation-drawer v-model="drawer">
      <v-list>
        <v-list-item v-for="(item, i) in items" :key="i" :value="item">
          <template v-slot:prepend>
            <v-icon :icon="item.icon"></v-icon>
          </template>

          <v-list-item-title>{{ item.name }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Globook</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <!--  -->
    </v-main>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    items: [
      { name: "Donate Book", icon: "mdi-book-plus" },
      { name: "Log catch", icon: "mdi-pin" },
      { name: "Explore books", icon: "mdi-magnify" },
    ],
  }),
};
</script>
