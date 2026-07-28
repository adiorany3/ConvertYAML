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
1. `AKUN-001-OVH-VLESS-WS-104MS` (url=257ms, nekobox=257ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-129MS` (url=344ms, nekobox=296ms, status=yes)
3. `AKUN-004-CLOUDFLARE-VLESS-WS-120MS` (url=227ms, nekobox=197ms, status=no)
4. `AKUN-003-CLOUDFLARE-VLESS-WS-138MS`
5. `AKUN-004-CLOUDFLARE-VLESS-WS-108MS`
6. `AKUN-005-CLOUDFLARE-VLESS-WS-151MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-161MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-162MS`
9. `AKUN-011-CLOUDFLARE-VLESS-WS-140MS` (url=270ms, nekobox=214ms, status=no)
10. `AKUN-008-UNKNOWN-VLESS-WS-161MS`
11. `AKUN-009-UNKNOWN-VLESS-WS-160MS`
12. `AKUN-010-CLOUDFLARE-VLESS-WS-150MS`
13. `AKUN-015-UNKNOWN-VLESS-WS-160MS` (url=326ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-178MS` (url=305ms, status=HTTP 204)
15. `AKUN-017-UNKNOWN-VLESS-WS-157MS` (url=300ms, status=HTTP 204)
16. `AKUN-018-UNKNOWN-VLESS-WS-145MS` (url=244ms, status=HTTP 204)
17. `AKUN-019-UNKNOWN-VLESS-WS-166MS` (url=308ms, status=HTTP 204)
18. `AKUN-020-RMGYVPN-VLESS-WS-157MS` (url=488ms, status=HTTP 204)
19. `AKUN-021-CLOUDFLARE-VLESS-WS-167MS` (url=228ms, status=HTTP 204)
20. `AKUN-023-UNKNOWN-VLESS-WS-344MS` (url=5645ms, status=HTTP 204)
21. `AKUN-025-CLOUDFLARE-VLESS-WS-268MS` (url=472ms, status=HTTP 204)
22. `AKUN-026-CLOUDFLARE-VLESS-WS-557MS` (url=1014ms, status=HTTP 204)
23. `AKUN-028-CLOUDFLARE-VLESS-WS-634MS` (url=978ms, status=HTTP 204)
24. `AKUN-029-CLOUDFLARE-VLESS-WS-672MS` (url=1022ms, status=HTTP 204)
25. `AKUN-032-SUKARIO-VLESS-WS-501MS` (url=992ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
