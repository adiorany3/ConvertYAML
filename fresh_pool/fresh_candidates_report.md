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
1. `AKUN-001-UNKNOWN-VLESS-WS-65MS` (url=225ms, nekobox=254ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-70MS` (url=245ms, nekobox=259ms, status=yes)
3. `AKUN-003-ALIBABA-VLESS-WS-77MS` (url=236ms, nekobox=256ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-95MS` (url=229ms, nekobox=259ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-68MS` (url=229ms, nekobox=261ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-66MS` (url=243ms, nekobox=257ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-92MS` (url=233ms, nekobox=261ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-111MS` (url=226ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-71MS` (url=230ms, nekobox=257ms, status=yes)
10. `AKUN-010-PUBLICDOMAINREGISTRY-NET-VLESS-WS-102MS` (url=277ms, nekobox=252ms, status=yes)
11. `AKUN-011-IDC-SG-VLESS-WS-120MS` (url=236ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-72MS` (url=271ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-68MS` (url=247ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-96MS` (url=248ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-94MS` (url=232ms, status=HTTP 204)
16. `AKUN-016-UNKNOWN-VLESS-WS-81MS` (url=230ms, status=HTTP 204)
17. `AKUN-017-466688-VLESS-WS-81MS` (url=251ms, status=HTTP 204)
18. `AKUN-019-1PASSWORD-VLESS-WS-81MS` (url=242ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-205MS` (url=429ms, status=HTTP 204)
20. `AKUN-021-UNKNOWN-VLESS-WS-256MS` (url=799ms, status=HTTP 204)
21. `AKUN-022-UNKNOWN-VLESS-WS-271MS` (url=658ms, status=HTTP 204)
22. `AKUN-024-UNKNOWN-VLESS-WS-291MS` (url=614ms, status=HTTP 204)
23. `AKUN-025-UNKNOWN-VLESS-WS-273MS` (url=3842ms, status=HTTP 204)
24. `AKUN-026-UNKNOWN-VLESS-WS-73MS` (url=236ms, status=HTTP 204)
25. `AKUN-027-UNKNOWN-VLESS-WS-71MS` (url=265ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
