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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-84MS` (url=217ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-86MS` (url=216ms, nekobox=248ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-83MS` (url=228ms, nekobox=260ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-98MS` (url=229ms, nekobox=235ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-86MS` (url=210ms, nekobox=232ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-112MS` (url=211ms, nekobox=210ms, status=no)
7. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-119MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-129MS`
9. `AKUN-008-ZVC-VLESS-WS-135MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-135MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-118MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-140MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-130MS` (url=216ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-112MS` (url=218ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-150MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-97MS` (url=284ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=215ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-112MS` (url=223ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-141MS` (url=245ms, status=HTTP 204)
20. `AKUN-020-RS-RAPIDSEEDBOX-20190717-VLESS-WS-209MS` (url=296ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-239MS` (url=5048ms, status=HTTP 204)
22. `AKUN-022-UNKNOWN-VLESS-WS-246MS` (url=530ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-88MS` (url=535ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-494MS` (url=829ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-510MS` (url=1285ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
