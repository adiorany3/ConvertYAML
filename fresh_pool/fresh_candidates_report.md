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
- Proxy di openclash_fresh_pool.yaml: 30

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
1. `AKUN-001-DE-XTOM-20190821-VLESS-WS-90MS` (url=213ms, nekobox=234ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-91MS` (url=248ms, nekobox=239ms, status=yes)
3. `AKUN-003-HGC-GLOBAL-COMMUNICATION-VLESS-WS-92MS` (url=208ms, nekobox=260ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-92MS` (url=209ms, nekobox=230ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-85MS` (url=235ms, nekobox=250ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-107MS` (url=218ms, nekobox=245ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-109MS` (url=213ms, nekobox=236ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-108MS` (url=221ms, nekobox=232ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-88MS` (url=206ms, nekobox=235ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-100MS` (url=257ms, nekobox=241ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-115MS` (url=210ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-113MS` (url=354ms, status=HTTP 204)
13. `AKUN-013-PUBLICDOMAINREGISTRY-NET-VLESS-WS-110MS` (url=217ms, status=HTTP 204)
14. `AKUN-014-US-VLESS-WS-116MS` (url=237ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-120MS` (url=240ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-140MS` (url=240ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-153MS` (url=236ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-220MS` (url=366ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-375MS` (url=3824ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-376MS` (url=788ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-369MS` (url=1691ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-372MS` (url=747ms, status=HTTP 204)
23. `AKUN-026-QZZ-VLESS-WS-582MS` (url=1070ms, status=HTTP 204)
24. `AKUN-027-CLOUDFLARE-VLESS-WS-680MS` (url=1196ms, status=HTTP 204)
25. `AKUN-028-GAMEFICTOINSPEED-VLESS-WS-757MS` (url=1138ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
