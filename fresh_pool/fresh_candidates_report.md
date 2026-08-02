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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-UNKNOWN-VLESS-WS-78MS` (url=215ms, nekobox=243ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-71MS` (url=220ms, nekobox=245ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-96MS` (url=224ms, nekobox=244ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=211ms, nekobox=247ms, status=yes)
5. `AKUN-005-877774-VLESS-WS-85MS` (url=219ms, nekobox=249ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-94MS` (url=210ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-100MS` (url=226ms, nekobox=182ms, status=no)
8. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-129MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-128MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-130MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-144MS` (url=277ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-262MS` (url=507ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-256MS` (url=612ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-163MS` (url=243ms, status=HTTP 204)
16. `AKUN-018-FASTVPSUS-IPV4-VLESS-WS-132MS` (url=273ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-414MS` (url=750ms, status=HTTP 204)
18. `AKUN-020-UNKNOWN-VLESS-WS-419MS` (url=668ms, status=HTTP 204)
19. `AKUN-021-UNKNOWN-VLESS-WS-358MS` (url=749ms, status=HTTP 204)
20. `AKUN-022-SUKARIO-VLESS-WS-408MS` (url=663ms, status=HTTP 204)
21. `AKUN-023-CLOUDFLARE-VLESS-WS-432MS` (url=1158ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-419MS` (url=717ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-426MS` (url=708ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-448MS` (url=714ms, status=HTTP 204)
25. `AKUN-030-UNKNOWN-VLESS-WS-557MS` (url=1376ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
