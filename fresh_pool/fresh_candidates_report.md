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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-70MS` (url=217ms, nekobox=248ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, nekobox=274ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-77MS` (url=206ms, nekobox=275ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-72MS` (url=207ms, nekobox=225ms, status=yes)
5. `AKUN-005-PUBLICDOMAINREGISTRY-NET-VLESS-WS-76MS` (url=233ms, nekobox=248ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-75MS` (url=205ms, nekobox=240ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-88MS` (url=210ms, nekobox=242ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-87MS` (url=206ms, nekobox=246ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-73MS` (url=206ms, nekobox=234ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-95MS` (url=225ms, nekobox=247ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-118MS` (url=209ms, status=HTTP 204)
12. `AKUN-012-WEBEX-VLESS-WS-121MS` (url=256ms, status=HTTP 204)
13. `AKUN-013-UNKNOWN-VLESS-WS-86MS` (url=209ms, status=HTTP 204)
14. `AKUN-014-PAGES-VLESS-WS-111MS` (url=198ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-108MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-98MS` (url=205ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-73MS` (url=236ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-99MS` (url=214ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-96MS` (url=226ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-156MS` (url=229ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-247MS` (url=530ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-236MS` (url=499ms, status=HTTP 204)
23. `AKUN-023-MICROSOFT-VLESS-WS-263MS` (url=576ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-288MS` (url=566ms, status=HTTP 204)
25. `AKUN-025-UNKNOWN-VLESS-WS-263MS` (url=513ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
