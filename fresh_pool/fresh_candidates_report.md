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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=245ms, nekobox=248ms, status=yes)
2. `AKUN-002-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=231ms, nekobox=265ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-63MS` (url=259ms, nekobox=261ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-66MS` (url=230ms, nekobox=260ms, status=yes)
5. `AKUN-005-OVH-VLESS-WS-75MS` (url=256ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=233ms, nekobox=279ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS` (url=223ms, nekobox=259ms, status=yes)
8. `AKUN-008-DIGITALOCEAN-VLESS-WS-85MS` (url=243ms, nekobox=276ms, status=yes)
9. `AKUN-009-WPENG-VLESS-WS-68MS` (url=232ms, nekobox=253ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-98MS` (url=247ms, nekobox=265ms, status=yes)
11. `AKUN-011-ZVC-VLESS-WS-104MS` (url=237ms, status=HTTP 204)
12. `AKUN-012-WEYRO-NET-VLESS-WS-110MS` (url=245ms, status=HTTP 204)
13. `AKUN-013-466688-VLESS-WS-79MS` (url=236ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-86MS` (url=240ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-110MS` (url=237ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-72MS` (url=240ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-90MS` (url=246ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-260MS` (url=687ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-256MS` (url=598ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-266MS` (url=607ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-285MS` (url=648ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-279MS` (url=574ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-285MS` (url=606ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-297MS` (url=625ms, status=HTTP 204)
25. `AKUN-026-UNKNOWN-VLESS-WS-411MS` (url=502ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
