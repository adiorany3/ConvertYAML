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
1. `AKUN-001-UNKNOWN-VLESS-WS-64MS` (url=215ms, nekobox=222ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-60MS` (url=209ms, nekobox=242ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=212ms, nekobox=235ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-68MS` (url=204ms, nekobox=942ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-63MS` (url=208ms, nekobox=236ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-70MS` (url=207ms, nekobox=889ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-81MS` (url=221ms, nekobox=227ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-62MS` (url=216ms, nekobox=227ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-77MS` (url=296ms, nekobox=243ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-79MS` (url=209ms, nekobox=238ms, status=yes)
11. `AKUN-012-CLOUDFLARE-VLESS-WS-75MS` (url=208ms, status=HTTP 204)
12. `AKUN-013-UNKNOWN-VLESS-WS-69MS` (url=203ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-97MS` (url=216ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-82MS` (url=218ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-107MS` (url=210ms, status=HTTP 204)
16. `AKUN-017-CLOUDFLARE-VLESS-WS-83MS` (url=205ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-103MS` (url=220ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-107MS` (url=208ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-81MS` (url=222ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-111MS` (url=218ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-112MS` (url=213ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-136MS` (url=217ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-150MS` (url=266ms, status=HTTP 204)
24. `AKUN-025-CLOUDFLARE-VLESS-WS-145MS` (url=230ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-89MS` (url=232ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
