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
1. `AKUN-001-UNKNOWN-VLESS-WS-66MS` (url=215ms, nekobox=242ms, status=yes)
2. `AKUN-002-ALIBABA-VLESS-WS-72MS` (url=222ms, nekobox=244ms, status=yes)
3. `AKUN-003-VULTR-VLESS-WS-85MS` (url=216ms, nekobox=305ms, status=yes)
4. `AKUN-004-VULTR-VLESS-WS-76MS` (url=203ms, nekobox=234ms, status=yes)
5. `AKUN-005-CLOUDFLARE-VLESS-WS-81MS` (url=232ms, nekobox=233ms, status=yes)
6. `AKUN-006-CLOUDFLARE-VLESS-WS-93MS` (url=229ms, nekobox=263ms, status=yes)
7. `AKUN-007-CLOUDFLARE-VLESS-WS-108MS` (url=218ms, nekobox=254ms, status=yes)
8. `AKUN-008-CLOUDFLARE-VLESS-WS-102MS` (url=220ms, nekobox=258ms, status=yes)
9. `AKUN-009-CLOUDFLARE-VLESS-WS-121MS` (url=227ms, nekobox=252ms, status=yes)
10. `AKUN-010-CLOUDFLARE-VLESS-WS-96MS`
11. `AKUN-012-CLOUDFLARE-VLESS-WS-255MS` (url=576ms, status=HTTP 204)
12. `AKUN-013-CLOUDFLARE-VLESS-WS-234MS` (url=552ms, status=HTTP 204)
13. `AKUN-014-UNKNOWN-VLESS-WS-265MS` (url=554ms, status=HTTP 204)
14. `AKUN-015-CLOUDFLARE-VLESS-WS-270MS` (url=507ms, status=HTTP 204)
15. `AKUN-016-CLOUDFLARE-VLESS-WS-249MS` (url=530ms, status=HTTP 204)
16. `AKUN-017-MICROSOFT-VLESS-WS-265MS` (url=564ms, status=HTTP 204)
17. `AKUN-029-CLOUDFLARE-VLESS-WS-233MS` (url=498ms, status=HTTP 204)
18. `AKUN-033-CLOUDFLARE-VLESS-WS-539MS` (url=882ms, status=HTTP 204)
19. `AKUN-034-CLOUDFLARE-VLESS-WS-592MS` (url=862ms, status=HTTP 204)

## Catatan
Fresh pool bukan pengganti AutoPilot. AutoPilot tetap memilih jalur sehat di router.
Fresh pool adalah cadangan siap-download ketika semua group utama mulai gagal berulang.
