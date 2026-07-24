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
1. `AKUN-001-UNKNOWN-VLESS-WS-76MS` (url=291ms, nekobox=309ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-78MS` (url=288ms, nekobox=302ms, status=yes)
3. `AKUN-003-CLOUDFLARE-VLESS-WS-82MS` (url=322ms, nekobox=317ms, status=yes)
4. `AKUN-004-UNKNOWN-VLESS-WS-98MS` (url=306ms, nekobox=313ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-109MS` (url=279ms, nekobox=372ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-79MS` (url=272ms, nekobox=317ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-88MS` (url=292ms, nekobox=320ms, status=yes)
8. `AKUN-008-UNKNOWN-VLESS-WS-117MS` (url=300ms, nekobox=436ms, status=yes)
9. `AKUN-009-UNKNOWN-VLESS-WS-111MS` (url=382ms, nekobox=327ms, status=yes)
10. `AKUN-010-UNKNOWN-VLESS-WS-95MS` (url=363ms, nekobox=315ms, status=yes)
11. `AKUN-011-CLOUDFLARE-VLESS-WS-124MS` (url=282ms, status=HTTP 204)
12. `AKUN-012-UNKNOWN-VLESS-WS-133MS` (url=299ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-123MS` (url=304ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-119MS` (url=380ms, status=HTTP 204)
15. `AKUN-015-CLOUDFLARE-VLESS-WS-126MS` (url=293ms, status=HTTP 204)
16. `AKUN-016-ZVC-VLESS-WS-118MS` (url=398ms, status=HTTP 204)
17. `AKUN-017-ZVC-VLESS-WS-135MS` (url=313ms, status=HTTP 204)
18. `AKUN-018-CLOUDFLARE-VLESS-WS-120MS` (url=278ms, status=HTTP 204)
19. `AKUN-019-CLOUDFLARE-VLESS-WS-159MS` (url=397ms, status=HTTP 204)
20. `AKUN-020-UNKNOWN-VLESS-WS-134MS` (url=319ms, status=HTTP 204)
21. `AKUN-021-UNKNOWN-VLESS-WS-153MS` (url=291ms, status=HTTP 204)
22. `AKUN-022-CLOUDFLARE-VLESS-WS-134MS` (url=361ms, status=HTTP 204)
23. `AKUN-023-CLOUDFLARE-VLESS-WS-182MS` (url=347ms, status=HTTP 204)
24. `AKUN-024-CLOUDFLARE-VLESS-WS-157MS` (url=423ms, status=HTTP 204)
25. `AKUN-025-CLOUDFLARE-VLESS-WS-286MS` (url=651ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
