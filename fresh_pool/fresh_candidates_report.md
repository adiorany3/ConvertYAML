# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 22
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 26

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-133MS` (url=254ms, nekobox=275ms, status=yes)
2. `AKUN-002-CLOUDFLARE-VLESS-WS-137MS` (url=265ms, nekobox=285ms, status=yes)
3. `AKUN-003-LEVIKOGJGFDD-VLESS-WS-142MS` (url=251ms, nekobox=280ms, status=yes)
4. `AKUN-004-CLOUDFLARE-VLESS-WS-141MS` (url=267ms, nekobox=308ms, status=yes)
5. `AKUN-005-UNKNOWN-VLESS-WS-139MS` (url=263ms, nekobox=273ms, status=yes)
6. `AKUN-006-UNKNOWN-VLESS-WS-143MS` (url=256ms, nekobox=286ms, status=yes)
7. `AKUN-007-UNKNOWN-VLESS-WS-138MS` (url=249ms, nekobox=292ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-141MS` (url=315ms, nekobox=281ms, status=yes)
9. `AKUN-009-LEVIKOGJGFDD-VLESS-WS-134MS`
10. `AKUN-010-FASTVPSUS-IPV4-VLESS-WS-186MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-188MS` (url=415ms, status=HTTP 204)
12. `AKUN-013-LEVIKOGJGFDD-VLESS-WS-131MS` (url=256ms, status=HTTP 204)
13. `AKUN-014-CLOUDFLARE-VLESS-WS-365MS` (url=663ms, status=HTTP 204)
14. `AKUN-016-CLOUDFLARE-VLESS-WS-416MS` (url=785ms, status=HTTP 204)
15. `AKUN-019-CLOUDFLARE-VLESS-WS-611MS` (url=2090ms, status=HTTP 204)
16. `AKUN-020-CLOUDFLARE-VLESS-WS-697MS` (url=1063ms, status=HTTP 204)
17. `AKUN-022-CLOUDFLARE-VLESS-WS-726MS` (url=1379ms, status=HTTP 204)
18. `AKUN-024-UNKNOWN-VLESS-WS-749MS` (url=1243ms, status=HTTP 204)
19. `AKUN-026-CLOUDFLARE-VLESS-WS-717MS` (url=1156ms, status=HTTP 204)
20. `AKUN-030-CLOUDFLARE-VLESS-WS-843MS` (url=2063ms, status=HTTP 204)
21. `AKUN-031-CLOUDFLARE-VLESS-WS-810MS` (url=1088ms, status=HTTP 204)
22. `AKUN-032-CLOUDFLARE-VLESS-WS-844MS` (url=1608ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
