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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS` (url=217ms, nekobox=237ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-65MS` (url=227ms, nekobox=238ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-67MS` (url=230ms, nekobox=245ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-73MS` (url=220ms, nekobox=243ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-76MS` (url=213ms, nekobox=242ms, status=yes)
6. `AKUN-006-WPENG-VLESS-WS-64MS` (url=224ms, nekobox=236ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-59MS` (url=216ms, nekobox=248ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-67MS` (url=210ms, nekobox=237ms, status=yes)
9. `AKUN-009-WEYRO-NET-VLESS-WS-72MS` (url=215ms, nekobox=254ms, status=yes)
10. `AKUN-010-INTERNETWORKS-45-131-6-0-VLESS-WS-101MS` (url=225ms, nekobox=229ms, status=yes)
11. `AKUN-011-WPENG-VLESS-WS-90MS` (url=228ms, status=HTTP 204)
12. `AKUN-012-TENCENT-VLESS-WS-111MS` (url=227ms, status=HTTP 204)
13. `AKUN-013-PAGES-VLESS-WS-70MS` (url=304ms, status=HTTP 204)
14. `AKUN-014-466688-VLESS-WS-82MS` (url=220ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-91MS` (url=210ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-358MS` (url=847ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-364MS` (url=729ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-370MS` (url=831ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-373MS` (url=792ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-385MS` (url=826ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-397MS` (url=867ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-435MS` (url=4207ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-350MS` (url=744ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-670MS` (url=1092ms, status=HTTP 204)
25. `AKUN-027-CLOUDFLARE-VLESS-WS-656MS` (url=1132ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
