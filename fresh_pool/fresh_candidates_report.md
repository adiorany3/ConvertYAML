# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 23
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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-59MS` (url=231ms, nekobox=243ms, status=yes)
2. `AKUN-002-PMBET-NET-VLESS-WS-70MS` (url=232ms, nekobox=259ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-58MS` (url=239ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-101MS` (url=247ms, nekobox=265ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-74MS` (url=217ms, nekobox=259ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-85MS` (url=213ms, nekobox=256ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=211ms, nekobox=254ms, status=yes)
8. `AKUN-008-WEYRO-NET-VLESS-WS-79MS` (url=224ms, nekobox=262ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-132MS` (url=266ms, nekobox=213ms, status=no)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-97MS` (url=227ms, nekobox=196ms, status=no)
11. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-75MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-148MS` (url=234ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=222ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-271MS` (url=413ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-353MS` (url=770ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-349MS` (url=725ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-379MS` (url=817ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-379MS` (url=943ms, status=HTTP 204)
20. `AKUN-022-UNKNOWN-VLESS-WS-464MS` (url=3427ms, status=HTTP 204)
21. `AKUN-025-UNKNOWN-VLESS-WS-68MS` (url=807ms, status=HTTP 204)
22. `AKUN-026-UNKNOWN-VLESS-WS-533MS` (url=840ms, status=HTTP 204)
23. `AKUN-027-CLOUDFLARE-VLESS-WS-669MS` (url=1128ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
