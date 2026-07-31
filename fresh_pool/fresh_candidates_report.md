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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-63MS` (url=203ms, nekobox=7177ms, status=no)
2. `AKUN-001-CLOUDFLARE-VLESS-WS-61MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-64MS`
4. `AKUN-003-UNKNOWN-VLESS-WS-68MS`
5. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-60MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-55MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-61MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-69MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS` (url=215ms, nekobox=205ms, status=no)
10. `AKUN-008-OVH-VLESS-WS-89MS`
11. `AKUN-009-CLOUDFLARE-VLESS-WS-68MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS`
13. `AKUN-013-CLOUDFLARE-VLESS-WS-79MS` (url=219ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-103MS` (url=209ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-79MS` (url=210ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-104MS` (url=224ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-80MS` (url=222ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-101MS` (url=207ms, status=HTTP 204)
19. `AKUN-019-DEV-VLESS-WS-131MS` (url=202ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-123MS` (url=202ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-111MS` (url=200ms, status=HTTP 204)
22. `AKUN-022-LEVIKOGJGFDD-VLESS-WS-103MS` (url=207ms, status=HTTP 204)
23. `AKUN-023-ACE-SG-VLESS-WS-97MS` (url=227ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-57MS` (url=198ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-106MS` (url=220ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
