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
1. `AKUN-001-DEV-VLESS-WS-85MS` (url=230ms, nekobox=256ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-89MS` (url=213ms, nekobox=232ms, status=yes)
3. `AKUN-003-DEV-VLESS-WS-89MS` (url=215ms, nekobox=240ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-83MS` (url=212ms, nekobox=233ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-87MS` (url=207ms, nekobox=191ms, status=no)
6. `AKUN-005-CLOUDFLARE-VLESS-WS-92MS`
7. `AKUN-006-UNKNOWN-VLESS-WS-84MS`
8. `AKUN-007-CHATGPT-VLESS-WS-95MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-106MS`
12. `AKUN-012-UNKNOWN-VLESS-WS-94MS` (url=270ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-107MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-134MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-103MS` (url=218ms, status=HTTP 204)
16. `AKUN-016-DEV-VLESS-WS-106MS` (url=214ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-142MS` (url=327ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-110MS` (url=205ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-151MS` (url=227ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-123MS` (url=209ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-127MS` (url=214ms, status=HTTP 204)
22. `AKUN-022-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-145MS` (url=219ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-94MS` (url=234ms, status=HTTP 204)
24. `AKUN-024-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-168MS` (url=1187ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-133MS` (url=270ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
