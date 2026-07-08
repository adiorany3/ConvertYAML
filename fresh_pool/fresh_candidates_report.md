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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-72MS` (url=222ms, nekobox=249ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-74MS` (url=224ms, nekobox=233ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-80MS` (url=233ms, nekobox=252ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-98MS` (url=221ms, nekobox=247ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-99MS` (url=210ms, nekobox=249ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-70MS` (url=211ms, nekobox=255ms, status=yes)
7. `AKUN-007-PUBLICDOMAINREGISTRY-NET-VLESS-WS-101MS` (url=222ms, nekobox=234ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-108MS` (url=199ms, nekobox=256ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-82MS` (url=227ms, nekobox=231ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-104MS` (url=215ms, nekobox=230ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-85MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-126MS` (url=205ms, status=HTTP 204)
13. `AKUN-013-WEBEX-VLESS-WS-71MS` (url=210ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-131MS` (url=210ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-97MS` (url=223ms, status=HTTP 204)
16. `AKUN-016-466688-VLESS-WS-106MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-129MS` (url=220ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-107MS` (url=210ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-237MS` (url=532ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-220MS` (url=518ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-269MS` (url=613ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-250MS` (url=563ms, status=HTTP 204)
23. `AKUN-023-UNKNOWN-VLESS-WS-276MS` (url=560ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-323MS` (url=441ms, status=HTTP 204)
25. `AKUN-028-UNKNOWN-VLESS-WS-440MS` (url=1112ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
