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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-89MS` (url=208ms, nekobox=233ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-89MS` (url=213ms, nekobox=226ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS` (url=200ms, nekobox=234ms, status=yes)
4. `AKUN-004-UK-GB-DCL-01-20191003-VLESS-WS-92MS` (url=209ms, nekobox=230ms, status=yes)
5. `AKUN-005-ZOOM-VLESS-WS-91MS` (url=208ms, nekobox=237ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-96MS` (url=230ms, nekobox=264ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-108MS` (url=198ms, nekobox=234ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-92MS` (url=210ms, nekobox=227ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-105MS` (url=248ms, nekobox=261ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-108MS` (url=202ms, nekobox=198ms, status=no)
11. `AKUN-010-COMPREND-NET-VLESS-WS-97MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-102MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-RS-RAPIDSEEDBOX-20190717-VLESS-WS-87MS` (url=213ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-157MS` (url=197ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-88MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-327MS` (url=571ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-369MS` (url=761ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-384MS` (url=740ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-391MS` (url=840ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-408MS` (url=814ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-399MS` (url=850ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-416MS` (url=823ms, status=HTTP 204)
23. `AKUN-026-UK-GB-DCL-01-20191003-VLESS-WS-268MS` (url=519ms, status=HTTP 204)
24. `AKUN-027-UNKNOWN-VLESS-WS-385MS` (url=799ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-716MS` (url=1152ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
