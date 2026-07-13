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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-65MS` (url=219ms, nekobox=248ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-66MS` (url=236ms, nekobox=253ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-66MS` (url=247ms, nekobox=265ms, status=yes)
4. `AKUN-004-RS-RAPIDSEEDBOX-20190717-VLESS-WS-73MS` (url=214ms, nekobox=243ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-85MS` (url=256ms, nekobox=288ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-82MS` (url=298ms, nekobox=274ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-89MS` (url=224ms, nekobox=297ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-85MS` (url=258ms, nekobox=265ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-89MS` (url=243ms, nekobox=301ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-70MS` (url=216ms, nekobox=243ms, status=yes)
11. `AKUN-011-ORG-VLESS-WS-88MS` (url=221ms, status=HTTP 204)
12. `AKUN-012-CLOUDFLARE-VLESS-WS-99MS` (url=222ms, status=HTTP 204)
13. `AKUN-013-PUBLICDOMAINREGISTRY-NET-VLESS-WS-125MS` (url=310ms, status=HTTP 204)
14. `AKUN-014-UNKNOWN-VLESS-WS-128MS` (url=236ms, status=HTTP 204)
15. `AKUN-015-HETZNER-VLESS-WS-104MS` (url=235ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-132MS` (url=238ms, status=HTTP 204)
17. `AKUN-017-CLOUDFLARE-VLESS-WS-114MS` (url=214ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-90MS` (url=234ms, status=HTTP 204)
19. `AKUN-019-HETZNER-VLESS-WS-143MS` (url=266ms, status=HTTP 204)
20. `AKUN-021-CLOUDFLARE-VLESS-WS-340MS` (url=776ms, status=HTTP 204)
21. `AKUN-022-CLOUDFLARE-VLESS-WS-368MS` (url=930ms, status=HTTP 204)
22. `AKUN-023-UNKNOWN-VLESS-WS-387MS` (url=1279ms, status=HTTP 204)
23. `AKUN-024-UNKNOWN-VLESS-WS-390MS` (url=847ms, status=HTTP 204)
24. `AKUN-028-CLOUDFLARE-VLESS-WS-280MS` (url=1007ms, status=HTTP 204)
25. `AKUN-029-DEV-VLESS-WS-614MS` (url=568ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
