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
1. `AKUN-001-ZVC-VLESS-WS-60MS` (url=257ms, nekobox=253ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-58MS` (url=229ms, nekobox=250ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-62MS` (url=236ms, nekobox=275ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-64MS` (url=371ms, nekobox=261ms, status=yes)
5. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-61MS` (url=227ms, nekobox=246ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-62MS` (url=289ms, nekobox=285ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-63MS` (url=228ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-65MS` (url=228ms, nekobox=254ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-70MS` (url=240ms, nekobox=261ms, status=yes)
10. `AKUN-010-EU-VLESS-WS-70MS` (url=250ms, nekobox=257ms, status=yes)
11. `AKUN-011-CL-173-242-112-0-20-VLESS-WS-75MS` (url=260ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-71MS` (url=564ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-69MS` (url=231ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-80MS` (url=228ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-99MS` (url=221ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-109MS` (url=220ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-74MS` (url=223ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-125MS` (url=235ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-95MS` (url=249ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-181MS` (url=327ms, status=HTTP 204)
21. `AKUN-021-CLOUDFLARE-VLESS-WS-125MS` (url=354ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-111MS` (url=283ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-251MS` (url=573ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-170MS` (url=290ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-267MS` (url=2575ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
