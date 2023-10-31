import { A11y, Navigation } from 'swiper/modules'
import { SwiperOptions } from 'swiper/types'

export const sliderSettings: SwiperOptions = {
  modules: [Navigation, A11y],
  spaceBetween: 10,
  slidesPerView: 'auto',
  autoplay: false,
  loop: false
}
