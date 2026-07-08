# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 25
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 31

## Cara Pakai di OpenWrt
Jalankan manual saat node mulai mati:

```sh
sh /etc/mihomo-autopilot/openwrt_pull_fresh_pool.sh
```

Atau aktifkan guard otomatis:

```sh
sh /etc/mihomo-autopilot/openwrt_fresh_guard.sh
```

## Kandidat Fresh Teratas
1. `AKUN-001-CLOUDFLARE-VLESS-WS-107MS` (url=278ms, nekobox=288ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-118MS` (url=278ms, nekobox=328ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-105MS` (url=294ms, nekobox=297ms, status=yes)
4. `AKUN-004-WPENG-VLESS-WS-117MS` (url=281ms, nekobox=294ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-124MS` (url=265ms, nekobox=314ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-111MS` (url=306ms, nekobox=327ms, status=yes)
7. `AKUN-007-WPENG-VLESS-WS-103MS` (url=347ms, nekobox=339ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-133MS` (url=283ms, nekobox=320ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-124MS` (url=257ms, nekobox=335ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-142MS` (url=302ms, nekobox=300ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-144MS` (url=276ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-127MS` (url=349ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-162MS` (url=253ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-171MS` (url=261ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-127MS` (url=292ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-163MS` (url=313ms, status=HTTP 204)
17. `AKUN-018-ES-FORNEX-20160629-VLESS-WS-186MS` (url=257ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-177MS` (url=277ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-128MS` (url=251ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-178MS` (url=376ms, status=HTTP 204)
21. `AKUN-022-MYBB-VLESS-WS-117MS` (url=270ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-106MS` (url=262ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-301MS` (url=649ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-331MS` (url=624ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-329MS` (url=759ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
