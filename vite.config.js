import {defineConfig} from 'vite';

// Hash navigation keeps the document path unchanged. Relative asset URLs work
// both at the domain root and under /chatgpt-schedule-sdm/ on GitHub Pages.
export default defineConfig({base:'./'});
