# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 17
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 21

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
1. `AKUN-001-UNKNOWN-VLESS-WS-108MS` (url=303ms, nekobox=327ms, status=yes)
2. `AKUN-002-UNKNOWN-VLESS-WS-102MS` (url=306ms, nekobox=330ms, status=yes)
3. `AKUN-003-LEVIKOGJGFDD-VLESS-WS-110MS` (url=275ms, nekobox=313ms, status=yes)
4. `AKUN-004-ZVC-VLESS-WS-143MS` (url=282ms, nekobox=286ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-153MS`
6. `AKUN-006-HOSTINGER-VLESS-WS-139MS`
7. `AKUN-007-CLOUDFLARE-VLESS-WS-143MS`
8. `AKUN-008-CLOUDFLARE-VLESS-WS-159MS`
9. `AKUN-009-UNKNOWN-VLESS-WS-169MS`
10. `AKUN-010-CLOUDFLARE-VLESS-WS-171MS`
11. `AKUN-013-CLOUDFLARE-VLESS-WS-201MS` (url=392ms, status=HTTP 204)
12. `AKUN-014-CLOUDFLARE-VLESS-WS-174MS` (url=372ms, status=HTTP 204)
13. `AKUN-015-CLOUDFLARE-VLESS-WS-189MS` (url=360ms, status=HTTP 204)
14. `AKUN-018-UNKNOWN-VLESS-WS-330MS` (url=763ms, status=HTTP 204)
15. `AKUN-022-CLOUDFLARE-VLESS-WS-618MS` (url=751ms, status=HTTP 204)
16. `AKUN-023-CLOUDFLARE-VLESS-WS-608MS` (url=1020ms, status=HTTP 204)
17. `AKUN-034-DEV-VLESS-WS-125MS` (url=904ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
