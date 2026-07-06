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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-64MS` (url=228ms, nekobox=260ms, status=yes)
2. `AKUN-002-WPENG-VLESS-WS-63MS` (url=273ms, nekobox=260ms, status=yes)
3. `AKUN-003-ZVC-VLESS-WS-64MS` (url=219ms, nekobox=259ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-76MS` (url=227ms, nekobox=259ms, status=yes)
5. `AKUN-005-VULTR-VLESS-WS-70MS` (url=224ms, nekobox=260ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-76MS` (url=234ms, nekobox=253ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-86MS` (url=214ms, nekobox=257ms, status=yes)
8. `AKUN-008-RS-RAPIDSEEDBOX-20190717-VLESS-WS-90MS` (url=240ms, nekobox=252ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-92MS` (url=213ms, nekobox=245ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-99MS` (url=231ms, nekobox=257ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-67MS` (url=216ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-103MS` (url=237ms, status=HTTP 204)
13. `AKUN-013-WEYRO-NET-VLESS-WS-84MS` (url=223ms, status=HTTP 204)
14. `AKUN-014-ZVC-VLESS-WS-129MS` (url=289ms, status=HTTP 204)
15. `AKUN-015-WPENG-VLESS-WS-78MS` (url=340ms, status=HTTP 204)
16. `AKUN-017-UNKNOWN-VLESS-WS-343MS` (url=767ms, status=HTTP 204)
17. `AKUN-018-CONFLU-VLESS-WS-365MS` (url=778ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-378MS` (url=1072ms, status=HTTP 204)
19. `AKUN-020-CLOUDFLARE-VLESS-WS-380MS` (url=838ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-388MS` (url=873ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-381MS` (url=841ms, status=HTTP 204)
22. `AKUN-023-CLOUDFLARE-VLESS-WS-372MS` (url=811ms, status=HTTP 204)
23. `AKUN-024-CLOUDFLARE-VLESS-WS-137MS` (url=318ms, status=HTTP 204)
24. `AKUN-026-CLOUDFLARE-VLESS-WS-680MS` (url=1099ms, status=HTTP 204)
25. `AKUN-028-CLOUDFLARE-VLESS-WS-657MS` (url=1116ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
