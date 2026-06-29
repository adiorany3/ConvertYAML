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
1. `AKUN-001-UNKNOWN-VLESS-WS-63MS` (url=213ms, nekobox=246ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-85MS` (url=199ms, nekobox=244ms, status=yes)
3. `AKUN-003-RS-RAPIDSEEDBOX-20190717-VLESS-WS-70MS` (url=201ms, nekobox=251ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=224ms, nekobox=244ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-93MS` (url=224ms, nekobox=232ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-88MS` (url=203ms, nekobox=251ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-80MS` (url=221ms, nekobox=237ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-97MS` (url=216ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-105MS` (url=227ms, nekobox=242ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-96MS` (url=228ms, nekobox=224ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-100MS` (url=215ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-111MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-89MS` (url=239ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-107MS` (url=250ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=205ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-72MS` (url=223ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-115MS` (url=216ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-124MS` (url=391ms, status=HTTP 204)
19. `AKUN-019-COMPREND-NET-VLESS-WS-85MS` (url=237ms, status=HTTP 204)
20. `AKUN-020-CONFLU-VLESS-WS-236MS` (url=488ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-248MS` (url=491ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-266MS` (url=575ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-231MS` (url=500ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-265MS` (url=587ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-275MS` (url=579ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
