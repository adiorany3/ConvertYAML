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
1. `AKUN-001-ZVC-VLESS-WS-63MS` (url=228ms, nekobox=300ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-62MS` (url=268ms, nekobox=277ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-78MS` (url=249ms, nekobox=310ms, status=yes)
4. `AKUN-004-LEVIKOGJGFDD-VLESS-WS-84MS` (url=250ms, nekobox=303ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-80MS` (url=261ms, nekobox=471ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-120MS` (url=323ms, nekobox=365ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-85MS` (url=252ms, nekobox=257ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-131MS` (url=245ms, nekobox=298ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-110MS` (url=238ms, nekobox=293ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-130MS` (url=242ms, nekobox=268ms, status=yes)
11. `AKUN-011-EU-VLESS-WS-137MS` (url=330ms, status=HTTP 204)
12. `AKUN-012-HOSTINGER-VLESS-WS-107MS` (url=316ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-133MS` (url=255ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-137MS` (url=338ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-144MS` (url=297ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-118MS` (url=321ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-123MS` (url=286ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-143MS` (url=369ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-204MS` (url=358ms, status=HTTP 204)
20. `AKUN-020-CLOUDFLARE-VLESS-WS-217MS` (url=328ms, status=HTTP 204)
21. `AKUN-021-090227-VLESS-WS-133MS` (url=310ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-168MS` (url=356ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-282MS` (url=909ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-456MS` (url=742ms, status=HTTP 204)
25. `AKUN-026-CLOUDFLARE-VLESS-WS-429MS` (url=663ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
