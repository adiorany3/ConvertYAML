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
1. `AKUN-001-UNKNOWN-VLESS-WS-54MS` (url=227ms, nekobox=236ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-63MS` (url=212ms, nekobox=236ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-61MS` (url=206ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-56MS` (url=207ms, nekobox=241ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-58MS` (url=210ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-54MS` (url=211ms, nekobox=234ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-61MS` (url=208ms, nekobox=239ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-62MS` (url=225ms, nekobox=235ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-61MS` (url=229ms, nekobox=171ms, status=no)
10. `AKUN-009-CLOUDFLARE-VLESS-WS-58MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-113MS`
12. `AKUN-014-CLOUDFLARE-VLESS-WS-66MS` (url=230ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-136MS` (url=225ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-67MS` (url=212ms, status=HTTP 204)
15. `AKUN-017-CLOUDFLARE-VLESS-WS-90MS` (url=225ms, status=HTTP 204)
16. `AKUN-018-ZVC-VLESS-WS-125MS` (url=218ms, status=HTTP 204)
17. `AKUN-019-CLOUDFLARE-VLESS-WS-65MS` (url=216ms, status=HTTP 204)
18. `AKUN-020-CLOUDFLARE-VLESS-WS-344MS` (url=772ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-57MS` (url=229ms, status=HTTP 204)
20. `AKUN-022-RS-RAPIDSEEDBOX-20190717-VLESS-WS-337MS` (url=1189ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-336MS` (url=774ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-359MS` (url=765ms, status=HTTP 204)
23. `AKUN-025-CLOUDFLARE-VLESS-WS-632MS` (url=1076ms, status=HTTP 204)
24. `AKUN-032-CLOUDFLARE-VLESS-WS-849MS` (url=1777ms, status=HTTP 204)
25. `AKUN-033-CLOUDFLARE-VLESS-WS-832MS` (url=1905ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
