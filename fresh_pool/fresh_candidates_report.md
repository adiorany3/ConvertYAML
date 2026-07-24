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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-100MS` (url=212ms, nekobox=245ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-108MS` (url=232ms, nekobox=232ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-101MS` (url=221ms, nekobox=255ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-93MS` (url=205ms, nekobox=245ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-99MS` (url=205ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-123MS` (url=201ms, nekobox=240ms, status=yes)
7. `AKUN-007-SPEEDTEST-VLESS-WS-136MS` (url=210ms, nekobox=214ms, status=no)
8. `AKUN-007-RS-RAPIDSEEDBOX-20190717-VLESS-WS-147MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-128MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-157MS`
12. `AKUN-012-LEVIKOGJGFDD-VLESS-WS-137MS` (url=223ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-111MS` (url=215ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-174MS` (url=229ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-113MS` (url=284ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-176MS` (url=249ms, status=HTTP 204)
17. `AKUN-017-ZOOM-VLESS-WS-135MS` (url=219ms, status=HTTP 204)
18. `AKUN-018-SPEEDTEST-VLESS-WS-162MS` (url=722ms, status=HTTP 204)
19. `AKUN-019-NET-141-11-202-0-23-VLESS-WS-355MS` (url=776ms, status=HTTP 204)
20. `AKUN-020-LEVIKOGJGFDD-VLESS-WS-369MS` (url=751ms, status=HTTP 204)
21. `AKUN-021-RS-RAPIDSEEDBOX-20190717-VLESS-WS-380MS` (url=1230ms, status=HTTP 204)
22. `AKUN-022-SPEEDTEST-VLESS-WS-446MS` (url=400ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-573MS` (url=684ms, status=HTTP 204)
24. `AKUN-027-SUKARIO-VLESS-WS-729MS` (url=1090ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-725MS` (url=1328ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
