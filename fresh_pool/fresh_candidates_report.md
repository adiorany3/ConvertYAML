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
1. `AKUN-001-LEVIKOGJGFDD-VLESS-WS-66MS` (url=228ms, nekobox=257ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-84MS` (url=239ms, nekobox=268ms, status=yes)
3. `AKUN-003-UNKNOWN-VLESS-WS-77MS` (url=253ms, nekobox=292ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-70MS` (url=245ms, nekobox=297ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-79MS` (url=319ms, nekobox=256ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-63MS` (url=347ms, nekobox=217ms, status=no)
7. `AKUN-006-UNKNOWN-VLESS-WS-76MS`
8. `AKUN-007-UNKNOWN-VLESS-WS-88MS`
9. `AKUN-008-090227-VLESS-WS-110MS`
10. `AKUN-009-UNKNOWN-VLESS-WS-129MS`
11. `AKUN-010-UNKNOWN-VLESS-WS-92MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-117MS` (url=280ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-91MS` (url=271ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-133MS` (url=255ms, status=HTTP 204)
15. `AKUN-015-LEVIKOGJGFDD-VLESS-WS-168MS` (url=372ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-122MS` (url=314ms, status=HTTP 204)
17. `AKUN-018-CLOUDFLARE-VLESS-WS-208MS` (url=351ms, status=HTTP 204)
18. `AKUN-019-CLOUDFLARE-VLESS-WS-222MS` (url=446ms, status=HTTP 204)
19. `AKUN-020-UNKNOWN-VLESS-WS-219MS` (url=444ms, status=HTTP 204)
20. `AKUN-022-CLOUDFLARE-VLESS-WS-266MS` (url=549ms, status=HTTP 204)
21. `AKUN-026-UNKNOWN-VLESS-WS-317MS` (url=532ms, status=HTTP 204)
22. `AKUN-027-CLOUDFLARE-VLESS-WS-433MS` (url=958ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-422MS` (url=712ms, status=HTTP 204)
24. `AKUN-030-UNKNOWN-VLESS-WS-530MS` (url=861ms, status=HTTP 204)
25. `AKUN-032-CLOUDFLARE-VLESS-WS-539MS` (url=1340ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
