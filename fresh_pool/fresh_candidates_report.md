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
1. `AKUN-001-UNKNOWN-VLESS-WS-89MS` (url=204ms, nekobox=238ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-92MS` (url=235ms, nekobox=235ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-95MS` (url=208ms, nekobox=235ms, status=yes)
4. `AKUN-004-PUBLICDOMAINREGISTRY-NET-VLESS-WS-97MS` (url=245ms, nekobox=248ms, status=yes)
5. `AKUN-005-ZOOM-VLESS-WS-98MS` (url=241ms, nekobox=264ms, status=yes)
6. `AKUN-006-466688-VLESS-WS-98MS` (url=223ms, nekobox=316ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-99MS` (url=223ms, nekobox=237ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-103MS` (url=219ms, nekobox=240ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-113MS` (url=238ms, nekobox=259ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-110MS` (url=211ms, nekobox=243ms, status=yes)
11. `AKUN-011-UNKNOWN-VLESS-WS-100MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-US-VLESS-WS-111MS` (url=218ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-129MS` (url=232ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-134MS` (url=249ms, status=HTTP 204)
15. `AKUN-015-DMIT-CUSTOMER-US-CA-9001-VLESS-WS-149MS` (url=211ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-144MS` (url=226ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-146MS` (url=266ms, status=HTTP 204)
18. `AKUN-018-UNKNOWN-VLESS-WS-138MS` (url=230ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-163MS` (url=379ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-201MS` (url=228ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-145MS` (url=219ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-132MS` (url=249ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-363MS` (url=1176ms, status=HTTP 204)
24. `AKUN-024-UNKNOWN-VLESS-WS-371MS` (url=859ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-381MS` (url=866ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
