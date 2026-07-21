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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=245ms, nekobox=258ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-62MS` (url=242ms, nekobox=268ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=230ms, nekobox=267ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-71MS` (url=245ms, nekobox=256ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-88MS` (url=240ms, nekobox=261ms, status=yes)
6. `AKUN-006-RS-RAPIDSEEDBOX-20190717-VLESS-WS-82MS` (url=220ms, nekobox=304ms, status=yes)
7. `AKUN-007-ZVC-VLESS-WS-95MS` (url=234ms, nekobox=275ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-84MS` (url=241ms, nekobox=279ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-94MS` (url=232ms, nekobox=270ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-76MS` (url=437ms, nekobox=289ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-122MS` (url=244ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-129MS` (url=261ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-134MS` (url=266ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-121MS` (url=219ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-131MS` (url=244ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-133MS` (url=250ms, status=HTTP 204)
17. `AKUN-017-UNKNOWN-VLESS-WS-127MS` (url=253ms, status=HTTP 204)
18. `AKUN-019-UNKNOWN-VLESS-WS-139MS` (url=262ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-105MS` (url=283ms, status=HTTP 204)
20. `AKUN-021-ZOOM-VLESS-WS-87MS` (url=274ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-271MS` (url=742ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-264MS` (url=4556ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-275MS` (url=5029ms, status=HTTP 204)
24. `AKUN-025-UNKNOWN-VLESS-WS-317MS` (url=640ms, status=HTTP 204)
25. `AKUN-031-CLOUDFLARE-VLESS-WS-480MS` (url=824ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
