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
1. `AKUN-001-UNKNOWN-VLESS-WS-62MS` (url=208ms, nekobox=238ms, status=yes)
2. `AKUN-002-ORACLE-VLESS-WS-67MS` (url=206ms, nekobox=250ms, status=yes)
3. `AKUN-003-INTERNETWORKS-45-131-6-0-VLESS-WS-72MS` (url=228ms, nekobox=254ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-71MS` (url=210ms, nekobox=239ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=230ms, nekobox=190ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-64MS`
7. `AKUN-006-OVH-VLESS-WS-69MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-73MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-94MS`
11. `AKUN-010-WEBEX-VLESS-WS-79MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-88MS` (url=196ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-64MS` (url=257ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-109MS` (url=213ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-81MS` (url=237ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-161MS` (url=216ms, status=HTTP 204)
17. `AKUN-017-PAGES-VLESS-WS-173MS` (url=230ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-240MS` (url=531ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-234MS` (url=518ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-258MS` (url=566ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-256MS` (url=497ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-252MS` (url=542ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-253MS` (url=568ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-252MS` (url=507ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-285MS` (url=707ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
