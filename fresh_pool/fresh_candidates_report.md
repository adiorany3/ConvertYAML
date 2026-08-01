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
- Proxy di openclash_fresh_pool.yaml: 29

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=210ms, nekobox=231ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-88MS` (url=199ms, nekobox=238ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-89MS` (url=230ms, nekobox=200ms, status=no)
4. `AKUN-003-UNKNOWN-VLESS-WS-84MS`
5. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS` (url=204ms, nekobox=224ms, status=no)
6. `AKUN-004-CLOUDFLARE-VLESS-WS-96MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-102MS` (url=198ms, nekobox=189ms, status=no)
8. `AKUN-005-CLOUDFLARE-VLESS-WS-95MS`
9. `AKUN-006-UNKNOWN-VLESS-WS-94MS`
10. `AKUN-007-CLOUDFLARE-VLESS-WS-98MS`
11. `AKUN-008-DEV-VLESS-WS-107MS`
12. `AKUN-009-UNKNOWN-VLESS-WS-107MS`
13. `AKUN-010-UNKNOWN-VLESS-WS-90MS`
14. `AKUN-014-CLOUDFLARE-VLESS-WS-92MS` (url=211ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-89MS` (url=198ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-115MS` (url=206ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-92MS` (url=225ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-102MS` (url=249ms, status=HTTP 204)
19. `AKUN-019-UNKNOWN-VLESS-WS-99MS` (url=215ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-94MS` (url=239ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-116MS` (url=252ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-94MS` (url=207ms, status=HTTP 204)
23. `AKUN-023-ZENFO-1-VLESS-WS-82MS` (url=210ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-311MS` (url=645ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-631MS` (url=984ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
