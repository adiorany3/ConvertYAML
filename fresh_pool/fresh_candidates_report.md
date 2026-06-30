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
1. `AKUN-001-ALIBABA-VLESS-WS-105MS` (url=212ms, nekobox=252ms, status=yes)
2. `AKUN-002-VULTR-VLESS-WS-103MS` (url=239ms, nekobox=243ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-99MS` (url=342ms, nekobox=255ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-117MS` (url=242ms, nekobox=268ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-101MS` (url=233ms, nekobox=284ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-121MS` (url=234ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-129MS` (url=251ms, nekobox=291ms, status=yes)
8. `AKUN-008-ZOOM-VLESS-WS-99MS` (url=216ms, nekobox=274ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-141MS` (url=298ms, nekobox=286ms, status=yes)
10. `AKUN-010-AEZA-NETWORK-VLESS-WS-118MS` (url=299ms, nekobox=294ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-136MS` (url=263ms, status=HTTP 204)
12. `AKUN-012-COMPREND-NET-VLESS-WS-129MS` (url=248ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-108MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-COMPREND-NET-VLESS-WS-173MS` (url=296ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-235MS` (url=449ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-395MS` (url=768ms, status=HTTP 204)
17. `AKUN-017-CONFLU-VLESS-WS-387MS` (url=1629ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-403MS` (url=787ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-400MS` (url=1002ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-415MS` (url=878ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-421MS` (url=872ms, status=HTTP 204)
22. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-419MS` (url=834ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-442MS` (url=875ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-300MS` (url=1201ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-802MS` (url=1379ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
