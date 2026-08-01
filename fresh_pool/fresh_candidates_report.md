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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-86MS` (url=208ms, nekobox=273ms, status=yes)
2. `AKUN-002-IP-VLESS-WS-89MS` (url=210ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-90MS` (url=226ms, nekobox=267ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-95MS` (url=225ms, nekobox=241ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-94MS` (url=213ms, nekobox=242ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-98MS` (url=215ms, nekobox=243ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-87MS` (url=218ms, nekobox=251ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-88MS` (url=217ms, nekobox=248ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-103MS` (url=234ms, nekobox=266ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-93MS` (url=244ms, nekobox=239ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-83MS` (url=223ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-115MS` (url=224ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-85MS` (url=276ms, status=HTTP 204)
14. `AKUN-014-MEDIUM-VLESS-WS-90MS` (url=217ms, status=HTTP 204)
15. `AKUN-015-ALIBABA-VLESS-WS-105MS` (url=236ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-139MS` (url=210ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-137MS` (url=210ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-126MS` (url=240ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-317MS` (url=611ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-616MS` (url=1010ms, status=HTTP 204)
21. `AKUN-023-UNKNOWN-VLESS-WS-642MS` (url=1033ms, status=HTTP 204)
22. `AKUN-024-CLOUDFLARE-VLESS-WS-679MS` (url=1122ms, status=HTTP 204)
23. `AKUN-026-CLOUDFLARE-VLESS-WS-759MS` (url=1214ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-730MS` (url=1175ms, status=HTTP 204)
25. `AKUN-029-UNKNOWN-VLESS-WS-779MS` (url=1242ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
