// Cronograma QPS 2026

const btnTopo = document.getElementById('btn-topo');

window.addEventListener('scroll', () => {
  if (btnTopo) btnTopo.classList.toggle('visible', window.scrollY > 400);
});

if (btnTopo) {
  btnTopo.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}
