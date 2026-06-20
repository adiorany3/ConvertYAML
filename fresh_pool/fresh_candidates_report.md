# Fresh Candidate Pool

File ini dibuat otomatis oleh GitHub Actions setelah node diuji.
Tujuannya: OpenWrt punya cadangan config/node fresh sebelum semua node utama mati.

## Output Fresh Pool
- `openclash_fresh_pool.yaml`: config darurat berisi kandidat fresh yang sudah lolos test GitHub.
- `fresh_pool/fresh_candidates.txt`: link akun kandidat fresh hasil URL test Mihomo.
- `fresh_pool/fresh_candidates_strict.txt`: link akun yang lolos sampai test NekoBox/sing-box.
- `fresh_pool/fresh_candidates.json`: metadata ringkas fresh pool.

## Ringkasan
- Kandidat fresh URL-tested: 19
- Kandidat strict NekoBox-tested: 10
- Proxy di openclash_fresh_pool.yaml: 25

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
1. `AKUN-001-CLOUDFLARE-VLESS-WS-83MS` (url=212ms, nekobox=7176ms, status=no)
2. `AKUN-001-RS-RAPIDSEEDBOX-20190717-VLESS-WS-86MS`
3. `AKUN-002-CLOUDFLARE-VLESS-WS-83MS`
4. `AKUN-003-VULTR-VLESS-WS-82MS`
5. `AKUN-004-ALIBABA-VLESS-WS-97MS`
6. `AKUN-005-RS-RAPIDSEEDBOX-20190717-VLESS-WS-117MS`
7. `AKUN-006-CLOUDFLARE-VLESS-WS-123MS`
8. `AKUN-007-CLOUDFLARE-VLESS-WS-91MS`
9. `AKUN-008-CLOUDFLARE-VLESS-WS-136MS`
10. `AKUN-009-CLOUDFLARE-VLESS-WS-256MS`
11. `AKUN-010-CLOUDFLARE-VLESS-WS-262MS`
12. `AKUN-012-CLOUDFLARE-VLESS-WS-263MS` (url=571ms, status=HTTP 204)
13. `AKUN-013-CLOUDFLARE-VLESS-WS-272MS` (url=571ms, status=HTTP 204)
14. `AKUN-014-CLOUDFLARE-VLESS-WS-277MS` (url=507ms, status=HTTP 204)
15. `AKUN-015-UNKNOWN-VLESS-WS-279MS` (url=584ms, status=HTTP 204)
16. `AKUN-016-CLOUDFLARE-VLESS-WS-237MS` (url=497ms, status=HTTP 204)
17. `AKUN-029-UNKNOWN-VLESS-WS-457MS` (url=562ms, status=HTTP 204)
18. `AKUN-033-DEV-VLESS-WS-637MS` (url=1015ms, status=HTTP 204)
19. `AKUN-034-UNKNOWN-VLESS-WS-648MS` (url=1656ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
