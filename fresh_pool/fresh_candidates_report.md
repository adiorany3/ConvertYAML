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
1. `AKUN-001-UNKNOWN-VLESS-WS-70MS` (url=212ms, nekobox=246ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-76MS` (url=213ms, nekobox=256ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-88MS` (url=206ms, nekobox=249ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-87MS` (url=199ms, nekobox=245ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-73MS`
6. `AKUN-006-CLOUDFLARE-VLESS-WS-92MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-74MS`
8. `AKUN-008-ZVC-VLESS-WS-78MS`
9. `AKUN-009-CLOUDFLARE-VLESS-WS-74MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-78MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-103MS` (url=232ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-132MS` (url=239ms, status=HTTP 204)
13. `AKUN-014-090227-VLESS-WS-134MS` (url=327ms, status=HTTP 204)
14. `AKUN-015-UNKNOWN-VLESS-WS-85MS` (url=227ms, status=HTTP 204)
15. `AKUN-016-UNKNOWN-VLESS-WS-150MS` (url=275ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-163MS` (url=205ms, status=HTTP 204)
17. `AKUN-018-UNKNOWN-VLESS-WS-133MS` (url=236ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-104MS` (url=292ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-194MS` (url=224ms, status=HTTP 204)
20. `AKUN-024-CLOUDFLARE-VLESS-WS-234MS` (url=494ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-404MS` (url=666ms, status=HTTP 204)
22. `AKUN-027-UNKNOWN-VLESS-WS-467MS` (url=1009ms, status=HTTP 204)
23. `AKUN-028-ZABIDAT-VLESS-WS-460MS` (url=764ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-456MS` (url=683ms, status=HTTP 204)
25. `AKUN-031-DEV-VLESS-WS-85MS` (url=456ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
